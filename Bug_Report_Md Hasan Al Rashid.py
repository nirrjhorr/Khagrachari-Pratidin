# -----------------------------
# 0️⃣ Ensure required packages
# -----------------------------
import subprocess
import sys


def install_package(pkg):
    try:
        __import__(pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])


for pkg in ["pandas", "gdown"]:
    install_package(pkg)

# -----------------------------
# 1️⃣ Imports
# -----------------------------
import gdown
import pandas as pd
import re
import os
import io
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

# -----------------------------
# 2️⃣ Download CSV from Google Drive
# -----------------------------
csv_url = 'https://drive.google.com/uc?id=1Kznl1lbu6frX9tpnrsxEhP7DRB53rNvr'
csv_file = os.path.join(os.path.expanduser("~"), "Documents", "bug_report.csv")


# Handle stdout issue when running as a GUI EXE
if not sys.stdout:
    sys.stdout = io.StringIO()
if not sys.stderr:
    sys.stderr = io.StringIO()

try:
    gdown.download(csv_url, csv_file, quiet=True)  # use quiet=True to prevent console output
except Exception as e:
    messagebox.showerror("Download Error", f"Failed to download CSV:\n{e}")
    sys.exit()
# -----------------------------
# 3️⃣ Load CSV & preprocess
# -----------------------------
def load_and_clean_csv(file_path):
    df = pd.read_csv(file_path, quotechar='"', keep_default_na=False)

    # Remove empty rows
    df = df[df.apply(lambda row: row.astype(str).str.strip().sum() != '', axis=1)]

    # Skip rows where Bug Title is empty
    if 'Bug Title' in df.columns:
        df = df[df['Bug Title'].str.strip() != ""]

    # Normalize Bug ID
    if '#BUG ID' in df.columns:
        df['#BUG ID'] = df['#BUG ID'].apply(lambda x: f"{int(x):03}" if str(x).isdigit() else x)

    # Format Steps to Reproduce
    def format_steps(text):
        if not text or text.strip() == "":
            return "Not Available"
        text = text.replace("\\n", "\n").replace("\n", "\n")
        steps = re.split(r'\r?\n|\d+\.', text)
        steps = [s.strip() for s in steps if s.strip() != ""]
        return "\n".join([step for step in steps])

    if 'Steps to Reproduce' in df.columns:
        df['Steps to Reproduce'] = df['Steps to Reproduce'].apply(format_steps)

    # Screenshot links
    if 'Screenshot/Screenrecord' in df.columns:
        df['Screenshot/Screenrecord'] = df['Screenshot/Screenrecord'].apply(
            lambda x: x if str(x).startswith("http") else "Link not available"
        )

    df.fillna("Not Available", inplace=True)
    return df


df = load_and_clean_csv(csv_file)

# -----------------------------
# 4️⃣ GUI Setup
# -----------------------------
root = tk.Tk()
root.title("🪲 Bug Report Viewer")
root.geometry("1300x750")
root.configure(bg="#f4f4f4")

# --- Guidelines
guideline_frame = tk.Frame(root, bg="#f4f4f4")
guideline_frame.pack(pady=10)
tk.Label(guideline_frame, text="Double-click a row to view full bug details.", font=("Arial", 14, "bold"),
         bg="#f4f4f4").pack()
tk.Label(guideline_frame, text="Filter by Bug ID or Severity.", font=("Arial", 12), bg="#f4f4f4").pack()

# --- Controls
control_frame = tk.Frame(root, bg="#f4f4f4")
control_frame.pack(pady=5)

tk.Label(control_frame, text="Search by Bug ID:", bg="#f4f4f4").grid(row=0, column=0, padx=5)
bug_id_entry = tk.Entry(control_frame, width=10)
bug_id_entry.grid(row=0, column=1, padx=5)
tk.Button(control_frame, text="Search", command=lambda: search_by_id()).grid(row=0, column=2, padx=5)
tk.Button(control_frame, text="Show All", command=lambda: update_table(df)).grid(row=0, column=3, padx=5)

tk.Label(control_frame, text="Filter by Severity:", bg="#f4f4f4").grid(row=0, column=4, padx=5)
tk.Button(control_frame, text="LOW", bg="#c6f6d5", command=lambda: filter_severity("LOW")).grid(row=0, column=5, padx=2)
tk.Button(control_frame, text="MEDIUM", bg="#fde68a", command=lambda: filter_severity("MEDIUM")).grid(row=0, column=6, padx=2)
tk.Button(control_frame, text="HIGH", bg="#fecaca", command=lambda: filter_severity("HIGH")).grid(row=0, column=7, padx=2)

# -----------------------------
# 5️⃣ Table with Beautiful Style
# -----------------------------
style = ttk.Style()
style.theme_use("clam")

# Table heading style
style.configure("Treeview.Heading",
                font=("Arial", 12, "bold"),
                background="#d1d5db",
                foreground="black")

# Table row style
style.configure("Treeview",
                font=("Arial", 11),
                rowheight=35,
                background="#f8fafc",
                fieldbackground="#f8fafc")

style.map("Treeview",
          background=[("selected", "#93c5fd")],
          foreground=[("selected", "black")])

columns = list(df.columns)
tree_frame = tk.Frame(root)
tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

# Scrollbars
scroll_y = ttk.Scrollbar(tree_frame, orient="vertical")
scroll_x = ttk.Scrollbar(tree_frame, orient="horizontal")

tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=25,
                    yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)
scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")
tree.pack(fill="both", expand=True)

# Column configuration
for col in columns:
    width = 150
    if "Title" in col:
        width = 300
    elif "Steps" in col:
        width = 350
    elif "Expected" in col or "Actual" in col:
        width = 300
    elif "Severity" in col:
        width = 100
    tree.heading(col, text=col, anchor="w")
    tree.column(col, width=width, anchor="w")

# Row colors
tree.tag_configure('LOW', background="#c6f6d5")
tree.tag_configure('MEDIUM', background="#fde68a")
tree.tag_configure('HIGH', background="#fecaca")

# Alternating row stripes
def apply_stripes():
    for i, item in enumerate(tree.get_children()):
        if i % 2 == 0:
            tree.item(item, tags=("striped",) + tree.item(item, "tags"))
style.configure("Treeview", background="#ffffff")
style.map("Treeview", background=[("selected", "#a7f3d0")])

# -----------------------------
# 6️⃣ Table Functions
# -----------------------------
def update_table(dataframe):
    for i in tree.get_children():
        tree.delete(i)
    for _, row in dataframe.iterrows():
        severity = str(row.get("Severity", "")).upper()
        tag = severity if severity in ["LOW", "MEDIUM", "HIGH"] else ""
        tree.insert("", "end", values=list(row), tags=(tag,))
    apply_stripes()


def search_by_id():
    bug_id = bug_id_entry.get().strip()
    if not bug_id:
        messagebox.showinfo("Info", "Please enter a Bug ID.")
        return
    try:
        bug_id_norm = f"{int(bug_id):03}"
        filtered = df[df['#BUG ID'] == bug_id_norm]
        if filtered.empty:
            messagebox.showinfo("Result", f"No bug found with ID {bug_id}")
        else:
            update_table(filtered)
    except:
        messagebox.showerror("Error", "Invalid Bug ID! Enter a number like 5 or 005.")


def filter_severity(sev):
    filtered = df[df['Severity'].str.upper() == sev.upper()]
    if filtered.empty:
        messagebox.showinfo("Result", f"No bugs found with Severity {sev}")
    else:
        update_table(filtered)

# -----------------------------
# 7️⃣ Double Click Details View
# -----------------------------
def on_row_double_click(event):
    sel = tree.selection()
    if not sel:
        return
    item = sel[0]
    values = tree.item(item, "values")
    bug_dict = dict(zip(columns, values))

    win = tk.Toplevel(root)
    win.title(f"Bug ID {bug_dict.get('#BUG ID', '')}")
    win.geometry("900x500")
    win.configure(bg="#f9f9f9")

    tk.Label(win, text=f"Bug ID: {bug_dict.get('#BUG ID', '')}", font=("Arial", 14, "bold"), bg="#f9f9f9").pack(pady=5)

    text_area = tk.Text(win, wrap="word", font=("Arial", 11))
    text_area.pack(fill="both", expand=True, padx=5, pady=5)

    def insert_with_links(col_name, content):
        if col_name.lower() == "steps to reproduce":
            text_area.insert(tk.END, f"{col_name}:\n")
        else:
            text_area.insert(tk.END, f"{col_name}: ")
        urls = re.findall(r"(https?://[^\s]+)", content)
        if urls:
            last_idx = 0
            for u in urls:
                start = content.find(u, last_idx)
                text_area.insert(tk.END, content[last_idx:start])
                text_area.insert(tk.END, u, ("link",))
                last_idx = start + len(u)
            text_area.insert(tk.END, content[last_idx:] + "\n\n")
        else:
            text_area.insert(tk.END, content + "\n\n")

    for col in columns:
        insert_with_links(col, str(bug_dict.get(col, "Not Available")))

    text_area.tag_config("link", foreground="blue", underline=True)
    text_area.tag_bind("link", "<Button-1>", lambda e: webbrowser.open(text_area.get(tk.SEL_FIRST, tk.SEL_LAST)))
    text_area.config(state="disabled")


tree.bind("<Double-1>", on_row_double_click)

# -----------------------------
# 8️⃣ Initialize Table
# -----------------------------
update_table(df)

# -----------------------------
# 9️⃣ Run GUI
# -----------------------------
root.mainloop()

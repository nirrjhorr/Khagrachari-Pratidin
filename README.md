# 🐞 Bug Report Automation and Visualization Tool

**Author:** Md Hasan Al Rashid
**Organization:** Bangla Puzzle Ltd.
**Project Type:** QA Assessment Project

---

## 🧠 Overview

This project was developed as part of a **Quality Assurance (QA) assessment** for **Bangla Puzzle Ltd.**
It automates and simplifies the process of creating, managing, and visualizing bug reports through a graphical interface.

The system can:

* Load and parse bug data from **Excel (.xlsx)**, **CSV (.csv)**, or even **Google Drive sheets**.
* Display real-time bug summaries and analytics through a **Tkinter GUI**.
* Run as a **standalone Windows executable (.exe)** — no Python installation required.

This tool helps QA professionals, developers, and project managers who want to analyze bugs easily — even without strong technical or testing backgrounds.

---

## ✨ Features

* ✅ **Multi-format Compatibility:** Supports `.csv`, `.xlsx`, and `.xls` files.
* ✅ **Interactive GUI:** Built with **Tkinter** for smooth navigation and bug browsing.
* ✅ **Real-time Data View:** Instantly updates the displayed data when new reports are loaded.
* ✅ **Bug Summary Dashboard:** Displays severity counts and overall project health.
* ✅ **Standalone Executable:** Can run independently on Windows systems (no Python needed).
* ✅ **Extensible Design:** Easy to improve and adapt for other testing or SDLC workflows.

---

## 🧩 Project Approach

1. **Manual Testing Phase**

   * Conducted functional, UI/UX, and performance testing on the target website:
     🔗 [https://khagracharipratidin.com/](https://khagracharipratidin.com/)
   * Documented all identified bugs in structured Excel and CSV files.

2. **Automation & Visualization Phase**

   * Designed a **Python-based GUI** to load, parse, and visualize bug reports dynamically.
   * Implemented backend logic using **Pandas** for data handling and analysis.
   * Developed an intuitive **Tkinter GUI** for non-technical users.

3. **Packaging Phase**

   * Converted the Python script into an **executable (.exe)** using **PyInstaller**:

     ```bash
     pyinstaller --onefile --noconsole Bug_Report_MdHasanAlRashid.py
     ```
   * Ensured the `.exe` runs smoothly on any Windows machine.

---

## 🧰 Tools & Technologies

| Category             | Tool / Library                  |
| -------------------- | ------------------------------- |
| Programming Language | Python                          |
| GUI Framework        | Tkinter                         |
| Data Processing      | Pandas                          |
| Excel Integration    | OpenPyXL                        |
| Visualization        | Matplotlib / Seaborn (optional) |
| Packaging            | PyInstaller                     |
| Version Control      | Git & GitHub                    |
| IDE Used             | VS Code / PyCharm               |

---

## 📂 Project Structure

```
BugReportTool/
│
├── Bug_Report_MdHasanAlRashid.py       # Main Python file with Tkinter GUI
├── Bug_Report_MdHasanAlRashid.exe      # Standalone Windows executable
├── Bug_Report_MdHasanAlRashid.xlsx     # Excel bug report (manual testing)
├── sample_bug_data.csv                 # Example bug report in CSV format
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies (optional)
```

---

## 🚀 How to Run

### 🧾 Option 1: Run with Python

1. Install dependencies:

   ```bash
   pip install pandas openpyxl tkinter
   ```
2. Run the script:

   ```bash
   python Bug_Report_MdHasanAlRashid.py
   ```

### 💻 Option 2: Run Executable (No Python Needed)

1. Locate `Bug_Report_MdHasanAlRashid.exe`
2. Double-click to launch the tool
3. Use the “Browse File” button to select your bug report (Excel or CSV)

---

## 📊 Example Use Case

1. Load your bug report file (`.xlsx` or `.csv`)
2. View all bugs with details like:

   * Bug ID
   * Title / Summary
   * Steps to Reproduce
   * Expected vs Actual Result
   * Severity
3. Analyze data visually and export summaries if needed.

---

## 🔮 Future Enhancements

* 🌐 Integration with **JIRA / Trello** for live bug tracking
* 📈 Dynamic charts for severity and module-wise analysis
* 🔍 Advanced search and filter options in GUI
* 🧠 AI-based bug classification by severity and type
* ☁️ Cloud integration (Google Sheets, Firebase, etc.)
* 🧑‍🤝‍🧑 Multi-user dashboard with collaboration features

---

## 📜 Conclusion

This project showcases the complete QA lifecycle — from **manual bug detection** and **reporting** to **automation, visualization, and packaging**.
It is a practical, user-friendly tool for testers, QA engineers, and anyone involved in the **Software Development Life Cycle (SDLC)** who wants a simplified yet powerful bug analysis utility.

---

## 👨‍💻 Author

**Name:** Md Hasan Al Rashid
**Role:** QA Engineer / Developer
**LinkedIn:** [https://www.linkedin.com/in/nirrjhorr/](https://www.linkedin.com/in/nirrjhorr/)
**GitHub:** [https://github.com/nirrjhorr/](https://github.com/nirrjhorr/)
**Email:** [mdhasanxtech@gmail.com](mailto:mdhasanxtech@gmail.com)

---

## 🧾 License

This project is for educational and assessment purposes under **Bangla Puzzle Ltd.**
You may reuse and modify the code for learning or internal QA process improvement.

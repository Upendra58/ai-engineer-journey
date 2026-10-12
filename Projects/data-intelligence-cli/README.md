# 📊 Data Intelligence CLI

A Python command-line application that reads employee data from a CSV file, validates records, analyzes salary information, and generates a structured data intelligence report.

## 🚀 Features

- **CSV Data Reading:** Loads employee records from a CSV file.
- **Data Validation:** Validates required fields, employee age, salary, and non-empty values.
- **Salary Analysis:** Calculates total salary and average salary.
- **Department Insights:** Calculates salary totals and employee counts by department.
- **Highest-Paid Employee:** Identifies the highest-paid employee overall and within each department.
- **Formatted Reports:** Displays results in a readable command-line report.
- **Automated Testing:** Uses pytest to test the reader, validator, and analyzer modules.

## 🛠️ Tech Stack

- Python 3.12
- Python CSV module
- pytest
- Git and GitHub

## 📁 Project Structure

```text
data-intelligence-cli/
├── app/
│   ├── main.py
│   ├── readers.py
│   ├── validators.py
│   ├── analyzer.py
│   └── reports.py
├── data/
│   └── employees.csv
├── tests/
│   ├── test_readers.py
│   ├── test_validators.py
│   └── test_analyzer.py
├── .gitignore
└── README.md
```

> Adjust the tree if your actual folder structure differs.

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd data-intelligence-cli
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install pytest

```bash
python -m pip install pytest
```

## ▶️ Run the Application

From the project root, run the command that matches your actual layout:

```powershell
python main.py
```

If your entry point is inside the `app` package instead, use:

```powershell
python -m app.main
```

## 🧪 Run Tests

From the project root, execute:

```powershell
python -m pytest -v
```

The current test suite contains **12 passing tests** covering the analyzer, CSV reader, and validators.

## 📈 Sample Output

```text
========================================
DATA INTELLIGENCE REPORT
========================================

Employee Summary
----------------------------------------
Total Employees : 8
Total Salary    : ₹508,000
Average Salary  : ₹63,500

Highest-Paid Employee
----------------------------------------
Name       : Henry
Department : IT
Salary     : ₹90,000

Salary by Department
----------------------------------------
IT             : ₹295,000
HR             : ₹120,000
Finance        : ₹93,000

Employee Count by Department
----------------------------------------
IT             : 4
HR             : 2
Finance        : 2

Highest-Paid Employee by Department
----------------------------------------
IT             : Henry (₹90,000)
HR             : Bob (₹65,000)
Finance        : Grace (₹48,000)
```

## 🎯 Learning Outcomes

This project demonstrates practical Python development skills:

- Functions, loops, conditions, and dictionaries
- Reading and processing CSV data
- Input validation and exception handling
- Modular code organization
- Automated testing with pytest
- Version control using Git

## 🔮 Future Improvements

- Add command-line arguments to select input files.
- Support additional data analysis and filtering.
- Export reports to CSV or JSON.
- Improve error handling for missing files and invalid records.

---

**Status:** Core implementation complete, automated tests passing, and code pushed to GitHub.

Built as part of my Python and AI Engineer learning journey.

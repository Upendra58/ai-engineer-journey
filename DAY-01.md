# 🚀 Day 1 — Environment & Engineering Setup

**Date:** September 18, 2026  
**Phase:** Phase 0 — Environment Setup  
**Status:** 🟢 COMPLETE  
**Progress:** 100%

---

## 🎯 Objective

Set up a clean, isolated development environment for the AI Engineer Journey and establish a professional Git + GitHub workflow.

### Target

> Become a production-ready AI Engineer by **January 1, 2027**.

---

# 🐍 1. Python Setup

### Python Version

```text
Python 3.12.2



Verified using:

python --version
pip

Upgraded pip using:

python -m pip install --upgrade pip

Final version:

pip 26.2.1
📁 2. Project Workspace

Created the workspace:

C:\AI-Engineer-Journey

Project structure:

C:\AI-Engineer-Journey
└── ai-engineer-journey
    └── day-01-environment

The AI Engineer environment is kept separate from existing projects such as resume_analyser.

🧪 3. Virtual Environment

Created:

python -m venv .venv

Activated:

.\.venv\Scripts\Activate.ps1

Terminal showed:

(.venv)
Verification
python -c "import sys; print(sys.executable)"

Result:

C:\AI-Engineer-Journey\ai-engineer-journey\day-01-environment\.venv\Scripts\python.exe
Key lesson

A virtual environment keeps project dependencies isolated.

📦 4. Foundation Packages

Installed:

python -m pip install numpy pandas matplotlib jupyter requests python-dotenv
Packages
Package	Purpose
NumPy	Numerical computing
Pandas	Data manipulation
Matplotlib	Visualization
Jupyter	Interactive experiments
Requests	HTTP/API communication
python-dotenv	Environment variables and secrets
Verification
python -c "import numpy, pandas, matplotlib, requests, dotenv; print('All foundation packages working 🚀')"

Result:

All foundation packages working 🚀
💻 5. VS Code

Opened the project using:

code .

VS Code is the primary editor for this journey.

🧪 6. First Python Program

Created:

hello_ai.py

Code:

def main():
    print("🚀 AI Engineer Journey")
    print("Day 1: Environment Setup")
    print("Target: January 1, 2027")
    print("Learning mode: Learn → Build → Debug → Deploy")


if __name__ == "__main__":
    main()

Executed:

python hello_ai.py
Output
🚀 AI Engineer Journey
Day 1: Environment Setup
Target: January 1, 2027
Learning mode: Learn → Build → Debug → Deploy
📋 7. Dependency Management

Created:

requirements.txt

using:

pip freeze > requirements.txt
Why?

requirements.txt records the Python packages required by the project.

🛡️ 8. Git Safety

Created:

.gitignore

Contents:

.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.env.*
.vscode/
Important

The .venv/ directory must not be committed to Git.

Secret files such as .env must also remain outside Git.

📝 9. README

Created a visual portfolio README containing:

🎯 Mission
🧭 AI Engineer roadmap
📊 Progress tracker
🧠 Learning philosophy
📅 Day 1 checklist
🛠️ Technology stack
🚀 Upcoming projects
🎯 2027 goal
🐙 10. Git Repository

Initialized Git:

git init

Configured the project to use:

main

branch.

💾 11. First Git Commit

Staged:

git add .

Created the first commit:

git commit -m "Day 1: setup AI engineer environment"

Commit:

b9ad0c2

Message:

Day 1: setup AI engineer environment

Committed files:

.gitignore
README.md
hello_ai.py
requirements.txt

The .venv/ directory was correctly excluded.

☁️ 12. GitHub

Created the remote repository:

ai-engineer-journey

GitHub:

https://github.com/Upendra58/ai-engineer-journey

Connected local Git:

git remote add origin https://github.com/Upendra58/ai-engineer-journey.git

Changed branch:

git branch -M main

Pushed:

git push -u origin main
Result
main → origin/main

GitHub successfully contains the Day 1 project.

🧹 13. Final Validation

Checked:

git status

Final state:

On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

🟢 Repository clean and synchronized.

🧠 What I Learned Today
Python
Python versions
pip
Virtual environments
Installing packages
Python executable paths
Project Management
Workspace isolation
requirements.txt
.gitignore
Git
git init
git status
git add
git commit
git branch
git remote
git push
GitHub
Creating a repository
Connecting local Git to GitHub
Pushing the main branch
🔄 Engineering Workflow

This is the workflow I will follow throughout the journey:

        💡 IDEA
          ↓
       💻 CODE
          ↓
       🧪 TEST
          ↓
      🐛 DEBUG
          ↓
      📊 MEASURE
          ↓
      💾 COMMIT
          ↓
       ☁️ PUSH
          ↓
      📝 EXPLAIN
📂 Day 1 Project Structure
day-01-environment/
│
├── .gitignore
├── README.md
├── DAY-01.md
├── hello_ai.py
├── requirements.txt
└── .venv/
       🔒 Git ignored
🏁 Day 1 Definition of Done
 Python 3.12.2
 pip upgraded
 Workspace created
 Virtual environment created
 Virtual environment verified
 NumPy installed
 Pandas installed
 Matplotlib installed
 Jupyter installed
 Requests installed
 python-dotenv installed
 VS Code configured
 First Python program created
 requirements.txt created
 .gitignore created
 README created
 Git initialized
 First commit created
 GitHub repository created
 GitHub remote connected
 main branch pushed
 Working tree clean
🟢 Final Status
Component	Status
🐍 Python	🟢 Ready
🧪 Virtual Environment	🟢 Ready
📦 Dependencies	🟢 Ready
💻 VS Code	🟢 Ready
🐙 Git	🟢 Ready
☁️ GitHub	🟢 Ready
📚 Documentation	🟢 Ready
🎯 Day 1: 100% COMPLETE

Don't collect courses. Collect capabilities.
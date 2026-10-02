# Day 12 — Python Project Structure + Logging + Testing

## 🎯 Day 12 Goal

Build a small professional Python project using project structure, reusable modules, logging, error handling, pytest, automated unit tests, and a calculator application.

## Part 1 — Python Project Structure

### Definition
A Python project structure organizes application code, tests, and entry points into clear folders and files.

### Practice

Created:

```text
day12/
├── app/
│   ├── __init__.py
│   └── calculator.py
├── test/
│   └── test_calculator.py
└── main.py
```

Created reusable functions for add, subtract, multiply, divide, and percentage.

### Result

**Part 1 — Complete ✅**

## Part 2 — Logging

### Definition
Logging records useful information about what an application is doing while it runs.

### Practice

Used `logging.info()` and `logging.error()` and configured logging in `main.py`:

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

Tested operation logs and division-by-zero errors.

### Result

**Part 2 — Complete ✅**

## Part 3 — Testing with pytest

### Definition
Automated testing checks whether code produces expected results without manually testing every case.

### Practice

Installed and verified pytest 9.1.1.

The first pytest run exposed an import-path issue. Running:

```powershell
python -m pytest
```

successfully executed the tests using the active Python environment.

### Tests Written

```python
from app import calculator
import pytest

def test_add():
    assert calculator.add(3, 4) == 7

def test_subtract():
    assert calculator.subtract(3, 4) == -1

def test_multiply():
    assert calculator.multiply(3, 4) == 12

def test_percentage():
    assert calculator.percentage(20, 200) == 40

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)

def test_divide():
    assert calculator.divide(20, 10) == 2
```

### Result

**6 tests passed.**

**Part 3 — Complete ✅**

## Part 4 — Mini Project: Calculator Application

Built a menu-driven calculator supporting:

1. Add
2. Subtract
3. Multiply
4. Divide
5. Percentage
6. Exit

The application accepts user input, calls reusable calculator functions, prints the result, and stops after the selected operation.

Division by zero is handled with `try/except` and `ValueError`.

### Result

**Part 4 — Complete ✅**

## 🧠 Day 12 Key Takeaways

- Clean project structure separates application code from tests.
- Reusable functions make code easier to test and maintain.
- Logging provides useful application diagnostics.
- `raise ValueError(...)` communicates invalid input to the caller.
- `pytest` automates verification.
- `pytest.raises()` verifies expected errors.
- Tests should cover both successful operations and important failure cases.
- `python -m pytest` runs pytest through the active Python environment.

## 📝 Day 12 Assessment

- [x] Python project structure
- [x] Reusable modules
- [x] Logging
- [x] Custom log format
- [x] Error handling
- [x] pytest installation
- [x] Unit tests
- [x] `assert`
- [x] `pytest.raises()`
- [x] Calculator mini-project
- [x] 6 passing tests

## 📌 What I Actually Completed

**Day 12: 🟢 COMPLETE**

## 🔜 Next

Day 13 — Python Professional Practices + Git/Testing Workflow

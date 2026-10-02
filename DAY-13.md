# Day 13 — Python Professional Practices + Git Workflow

## 🎯 Day 13 Goal

Move from writing working Python code to writing clean, readable, maintainable engineering code.

---

## Part 1 — Clean Code & Naming

Learned to replace unclear names with meaningful function, parameter, and variable names.

Example:

```python
def higher_lower(number1, number2):
    total = number1 + number2

    if total > 50:
        print("Total is higher than 50")
    else:
        print("Total is lower than 50")
```

### Mentor Feedback

- Meaningful parameter names
- Meaningful variable name
- Corrected function naming
- Added explicit handling for the equality case
- Learned that function names should describe the purpose of the function

---

## Part 2 — Type Hints

Practiced parameter and return type annotations.

```python
def calculate_area(length: float, width: float) -> float:
    area = length * width
    return area
```

### Key Learning

Type hints communicate expected data types and improve readability, IDE support, static analysis, and maintainability.

---

## Part 3 — Docstrings

Learned to use one proper docstring immediately after a function definition.

```python
def calculate_discount(price: float, discount: float) -> float:
    """
    Calculate the final price after applying a percentage discount.

    price: Original price.
    discount: Discount percentage.
    """
    final_price = price - (price * discount / 100)
    return final_price
```

### Correction Learned

Multiple standalone string blocks are not a proper way to document a function. Use one clear docstring.

---

## Part 4 — Refactoring

### Definition

Refactoring means improving code structure and readability without changing its intended behavior.

Refactored unclear code into a function with:

- Meaningful function name
- Meaningful parameters
- Meaningful variables
- Type hints
- Docstring
- Clean formatting
- Explicit equality handling

Example:

```python
def analyze_total(number1: int, number2: int, number3: int) -> int:
    """
    Calculate the total of three numbers and compare it with 100.
    """
    total = number1 + number2 + number3

    if total > 100:
        print("Total is greater than 100")
    elif total < 100:
        print("Total is less than 100")
    else:
        print("Total is equal to 100")

    return total
```

---

## Part 5 — Practical Git Workflow

Checked the repository status and confirmed the working tree was initially clean.

Created:

```text
day13_code_quality/code1.py
```

Then checked Git status and saw the new folder as untracked.

Staged the Day 13 code with:

```bash
git add day13_code_quality/
```

Git confirmed:

```text
Changes to be committed:
    new file: day13_code_quality/code1.py
```

Git commit and push were already understood from previous work, so the focus remained on Python engineering practices.

---

## Part 6 — Practical Python Exercises

### Discount Calculation

Created and ran a typed Python function:

```python
def calculate_discount(price: float, discount: float) -> float:
    """
    Calculate the final price after applying a percentage discount.
    """
    final_price = price - (price * discount / 100)
    return final_price
```

Tested with:

```text
price = 1000
discount = 20
```

Result:

```text
800.0
```

Improved the program to display:

```text
Original price: 1000
Discount: 20%
Final price: 800.0
```

### Function Responsibility

Learned the difference between:

```python
-> float
```

for a function that returns a float, and:

```python
-> None
```

for a function that performs an action such as printing without returning a value.

### Final Independent Challenge

Created and ran:

```python
def calculate_salary(salary: float, bonus: float) -> float:
    bonus_amount = salary * bonus / 100
    final_salary = salary + bonus_amount
    return final_salary

salary = 50000
bonus = 10

final_salary = calculate_salary(salary, bonus)
print(final_salary)
```

Result:

```text
55000.0
```

---

## 🧠 Day 13 Key Takeaways

1. Meaningful names make code easier to understand.
2. Type hints communicate expected types.
3. Docstrings document the purpose of functions.
4. Refactoring improves maintainability.
5. Edge cases such as equality should be handled explicitly.
6. `-> float` indicates a returned float.
7. `-> None` is appropriate when a function performs an action without returning a value.
8. Practice should include writing, running, checking, and improving code.

---

## 📌 What I Actually Completed

- ✅ Clean code and meaningful naming
- ✅ Type hints
- ✅ Return type annotations
- ✅ Docstrings
- ✅ Refactoring
- ✅ Edge-case handling
- ✅ Writing and running Python functions
- ✅ Practical Git status
- ✅ Git staging
- ✅ Final independent coding challenge

---

## 🏁 Day 13 Status

**🟢 COMPLETE**

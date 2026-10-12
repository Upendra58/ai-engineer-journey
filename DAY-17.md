# Day 17 — Python Gaps + Data Intelligence CLI

## Status

**Day 17: COMPLETE**

Today closed the remaining high-priority Python language/tooling gaps and applied them while starting the first serious Python portfolio project.

## Python Concepts Closed

### 1. Mutability and Immutability
Mutable objects can be changed after creation. Examples: `list`, `dict`, `set`.

```python
numbers = [10, 20, 30]
numbers[1] = 200
print(numbers)
# [10, 200, 30]
```

Immutable examples include `int`, `float`, `str`, and `tuple`.

### 2. References and Object Identity
Assignment can make two names reference the same object.

```python
a = [10, 20, 30]
b = a
b[0] = 100

print(a)
print(b)
print(a is b)
# [100, 20, 30]
# [100, 20, 30]
# True
```

### 3. Shallow Copy

```python
a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 100
```

The outer list is copied, but nested mutable objects are still shared.

### 4. Deep Copy

```python
import copy

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)
b[0][0] = 100
```

Deep copy makes nested mutable objects independent.

### 5. Lambda

```python
double = lambda x: x * 2
print(double(5))
# 10
```

### 6. map()

```python
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))
# [2, 4, 6, 8]
```

### 7. filter()

```python
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))
# [2, 4, 6]
```

### 8. reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda a, b: a * b, numbers)
print(result)
# 24
```

### 9. Context Managers

A context manager manages setup and cleanup automatically.

```python
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
```

Common modes: `r` read, `w` write/replace, `a` append, `r+` read/write.

### 10. collections.Counter

```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]
counts = Counter(numbers)
print(counts.most_common(2))
```

Useful for frequency analysis.

### 11. defaultdict

```python
from collections import defaultdict

employees = [("Alice", "IT"), ("Bob", "HR"), ("Charlie", "IT")]
result = defaultdict(list)

for name, department in employees:
    result[department].append(name.upper())
```

Useful for grouping data.

### 12. deque

```python
from collections import deque

numbers = deque([10, 20, 30])
numbers.append(40)
numbers.appendleft(5)
numbers.popleft()
numbers.pop()
```

Useful for efficient operations at both ends.

### 13. Dataclasses

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total_price(self):
        return self.price * self.quantity
```

### 14. Advanced Type Hints

```python
def calculate_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)
```

Other examples: `list[str]`, `dict[str, int]`, `str | None`.

### 15. itertools

```python
from itertools import chain, combinations

numbers = chain([1, 2], [3, 4])
print(list(numbers))

print(list(combinations([1, 2, 3], 2)))
```

### 16. Memory Management Fundamentals

Python manages memory automatically using mechanisms including reference counting and garbage collection. Avoid unnecessary large copies; generators can help process data without holding everything in memory at once.

---

# Project 1 — Data Intelligence CLI

## Current structure

```text
data-intelligence-cli/
├── app/
│   ├── __init__.py
│   ├── readers.py
│   ├── validators.py
│   └── analyzer.py
├── data/
│   └── employees.csv
└── main.py
```

## Architecture

```text
employees.csv
     ↓
readers.py
     ↓
raw employee dictionaries
     ↓
validators.py
     ↓
clean employee data
     ↓
analyzer.py
     ↓
business insights
```

## CSV Reader

`readers.py` reads the file and returns a list of dictionaries.

```python
import csv


def read_csv(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
```

`main.py` supplies the actual file path:

```python
employees = read_csv("data/employees.csv")
```

## Validation

### Age

```python
def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a valid integer")

    if age <= 0:
        raise ValueError("Age must be greater than 0")

    if age > 100:
        raise ValueError("Age must be 100 or less")

    return age
```

### Salary

```python
def validate_salary(salary):
    try:
        salary = int(salary)
    except ValueError:
        raise ValueError("Salary must be a valid integer")

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    return salary
```

### Required fields

```python
def validate_required_fields(employee):
    required_fields = ["name", "age", "department", "salary"]

    for field in required_fields:
        if field not in employee:
            raise ValueError(f"Required field is missing: {field}")

    return employee
```

### Empty text fields

```python
def validate_non_empty_fields(employee):
    fields = ["name", "department"]

    for field in fields:
        if not employee[field].strip():
            raise ValueError(f"{field} cannot be empty")

    return employee
```

### One employee

```python
def validate_employee(employee):
    validate_required_fields(employee)
    validate_non_empty_fields(employee)

    employee["age"] = validate_age(employee["age"])
    employee["salary"] = validate_salary(employee["salary"])

    return employee
```

### Entire dataset

```python
def validate_employees(employees):
    validated_employees = []

    for employee in employees:
        validated_employee = validate_employee(employee)
        validated_employees.append(validated_employee)

    return validated_employees
```

## Analyzer

### Total salary

```python
def calculate_total_salary(employees):
    total = 0

    for employee in employees:
        total += employee["salary"]

    return total
```

### Average salary

```python
def calculate_average_salary(employees):
    if not employees:
        raise ValueError("Employee list cannot be empty")

    total_salary = calculate_total_salary(employees)
    average_salary = total_salary / len(employees)

    return average_salary
```

### Highest-paid employee

```python
def highest_paid_employee(employees):
    if not employees:
        raise ValueError("Employee list cannot be empty")

    highest_employee = employees[0]

    for employee in employees:
        if employee["salary"] > highest_employee["salary"]:
            highest_employee = employee

    return highest_employee
```

## Important Debugging Lesson

Do not overwrite a function name with its returned value.

Bad:

```python
validate_employees = validate_employees(employees)
```

Good:

```python
validated_employees = validate_employees(employees)
```

A function name should continue to refer to the function; use a separate variable for its result.

---

# Python Roadmap Status

**Core Python concepts: COMPLETE for the current roadmap.**

This does **not** mean Python portfolio completion is finished.

Portfolio requirement: **5–8 meaningful Python projects**.

Current completed Python projects: **0/8**.

Project 1 is currently **Building**, not complete.

## Day 17 Key Takeaways

1. Variables can share references to the same mutable object.
2. Shallow and deep copy solve different problems.
3. `lambda`, `map`, `filter`, and `reduce` are useful functional tools.
4. Context managers handle resource cleanup.
5. `Counter`, `defaultdict`, and `deque` are practical standard-library tools.
6. Dataclasses simplify structured models.
7. Type hints improve readability and maintainability.
8. `itertools` provides efficient iterator utilities.
9. Production Python requires validation and edge-case handling.
10. Keep function names separate from variables holding returned results.
11. Project-based implementation is now the main path for completing Python engineering skills.

**Status: 🟢 Day 17 COMPLETE**

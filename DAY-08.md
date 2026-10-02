# Day 8 — Exceptions, File Handling & JSON

## Focus
Learn exception handling and understand file/JSON handling.

## Completed
- Runtime errors and exceptions
- `try`, `except`, `else`, `finally`
- Multiple exception types
- `raise`
- Validation functions
- File handling concepts
- JSON concepts

## Exception Example
```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)
finally:
    print("Program finished")
```

## Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

## JSON
Covered:
- `json.loads()`
- `json.load()`
- `json.dumps()`
- `json.dump()`
- `json.JSONDecodeError`
- JSON object → Python dictionary
- JSON array → Python list

## Accuracy Note
Exception handling and `raise` were practiced directly. File handling and JSON were studied during the lesson but were not independently practiced to the same depth.

## Assessment
**Day 8: 🟢 COMPLETE**

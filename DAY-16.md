# 📝 Day 16 — Advanced Python: Comprehensions, Iterators, Generators & Decorators

## 🎯 Goal
Learn advanced Python language features and combine them in a practical employee data-processing program.

## 1. List Comprehensions
A **list comprehension** is a concise way to create a new list from an iterable, optionally applying a condition.

```python
[expression for item in iterable if condition]
```

Example:
```python
numbers = [10, 15, 20, 25, 30, 35, 40]
greater = [number for number in numbers if number > 20]
squares = [number * number for number in numbers if number > 20]
```

Other practice:
```python
numbers = [1,2,3,4,5,6,7,8,9,10]
even_squares = [number * number for number in numbers if number % 2 == 0]

names = ["alice","bob","charlie","david"]
upper_names = [name.upper() for name in names]
```

## 2. Dictionary Comprehension
A **dictionary comprehension** concisely creates a dictionary.

```python
names = ["alice", "bob", "charlie"]

name_length = {name: len(name) for name in names}
```

Conditional example:
```python
numbers = [1,2,3,4,5,6]
squares = {number: number * number for number in numbers if number % 2 == 0}
```

## 3. Set Comprehension
A **set comprehension** creates a set. Sets automatically remove duplicates.

```python
numbers = [1,2,3,4,5,6,6,4,2]
squares = {number * number for number in numbers if number % 2 == 0}
```

## 4. `*args`
`*args` allows a function to accept any number of positional arguments. `args` is only a conventional name; `*` is the important syntax.

```python
def calculate_sum(*args):
    total = 0
    for number in args:
        total += number
    return total

print(calculate_sum(10, 20, 30))
```

Inside the function, `args` is a tuple.

## 5. `**kwargs`
`**kwargs` allows a function to accept any number of keyword arguments. `kwargs` is conventional; `**` is the important syntax.

```python
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_profile(name="Upendra", age=26, role="AI Engineer")
```

Inside the function, `kwargs` is a dictionary.

## 6. Iterators
An **iterator** produces values one at a time and remembers its current position.

```python
numbers = [5, 10, 15]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

When exhausted, `next()` raises `StopIteration`.

**Iterable:** can provide an iterator, such as list, tuple, string, dict, or set.

**Iterator:** tracks position and produces the next value.

A `for` loop conceptually uses `iter()`, repeated `next()`, and handles `StopIteration`.

## 7. Generators
A **generator** is a special iterator that produces values one at a time using `yield`.

```python
def count_numbers():
    yield 1
    yield 2

numbers = count_numbers()
print(next(numbers))
print(next(numbers))
```

A generator is already an iterator.

Loop generator:
```python
def count_numbers():
    for number in range(1, 6):
        yield number
```

Infinite generator:
```python
def count_numbers():
    number = 1
    while True:
        yield number
        number += 1
```

`yield` produces a value, pauses the function, preserves its state, and continues later.

### Generator debugging lesson
Incorrect:
```python
def numbers():
    number = 1
    while True:
        if number % 2 == 0:
            yield number
            number += 1
```

When `number` is odd, it never increments and the generator gets stuck.

Correct:
```python
def numbers():
    number = 1
    while True:
        if number % 2 == 0:
            yield number
        number += 1
```

## 8. Decorators
A **decorator** is a function that takes another function, adds or changes its behavior, and returns a function.

Functions can be passed as objects:
```python
def greet():
    print("Hello")

def execute(function):
    function()

execute(greet)
```

Basic decorator:
```python
def my_decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")
    return wrapper
```

Using `@`:
```python
@my_decorator
def greet():
    print("Hello")
```

`@my_decorator` is conceptually:
```python
greet = my_decorator(greet)
```

## 9. Decorators with Arguments
Use `*args` and `**kwargs` so the wrapper can accept the original function's arguments.

```python
def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("Starting function")
        result = function(*args, **kwargs)
        print("Function finished")
        return result
    return wrapper
```

Returning `result` is important so the decorated function keeps its return value.

## 10. `functools.wraps`
`functools.wraps` preserves metadata such as the original function name and docstring.

```python
from functools import wraps

def log_function(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("started")
        result = function(*args, **kwargs)
        print("completed")
        return result
    return wrapper
```

```python
@log_function
def add(a, b):
    return a + b

print(add.__name__)  # add
```

## 11. Decorators with Their Own Arguments
```python
from functools import wraps

def repeat(times):
    def time_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)
        return wrapper
    return time_decorator
```

Usage:
```python
@repeat(3)
def greet():
    print("Hello")

greet()
```

## 12. Practical Employee Data Processor
```python
employees = [
    {"name": "Alice", "age": 25, "salary": 50000, "department": "IT"},
    {"name": "Bob", "age": 30, "salary": 65000, "department": "HR"},
    {"name": "Charlie", "age": 28, "salary": 75000, "department": "IT"},
    {"name": "David", "age": 24, "salary": 45000, "department": "Finance"},
    {"name": "Eve", "age": 32, "salary": 80000, "department": "IT"},
]
```

List comprehension:
```python
salary_g = [employee["name"] for employee in employees if employee["salary"] > 60000]
```

Dictionary comprehension:
```python
dict_s = {employee["name"]: employee["salary"] for employee in employees}
```

Set comprehension:
```python
set_s = {employee["department"] for employee in employees}
```

`*args`:
```python
def calculate_salary(*args):
    total_salary = 0
    for number in args:
        total_salary += number
    return total_salary
```

`**kwargs`:
```python
def show_employee(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
```

Generator:
```python
def employee_generator(employees):
    for employee in employees:
        yield employee
```

Average with decorator:
```python
def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("calculation started")
        result = function(*args, **kwargs)
        print("average calculation done")
        return result
    return wrapper

@my_decorator
def calculate_average(*args):
    total = 0
    for number in args:
        total += number
    average = total / len(args)
    return average
```

Final combined function:
```python
from functools import wraps

def log_function(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("started")
        result = function(*args, **kwargs)
        print("completed")
        return result
    return wrapper

def repeat(times):
    def time_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return time_decorator

@repeat(2)
@log_function
def show_high_salary_employees(employees, min_salary=60000):
    high_salary = [
        employee["name"]
        for employee in employees
        if employee["salary"] > min_salary
    ]
    return high_salary

print(show_high_salary_employees(employees))
```

Output:
```text
started
completed
started
completed
['Bob', 'Charlie', 'Eve']
```

## 🐛 Important Debugging Lesson
When the final result was `None`, the issue was the `repeat()` decorator calling the function without returning its result.

Fix:
```python
result = function(*args, **kwargs)
# ...
return result
```

A wrapper should normally preserve the original function's return value unless intentionally changing it.

## 🧠 Cheat Sheet

| Concept | Key idea |
|---|---|
| List comprehension | Concise list creation |
| Dict comprehension | Concise dictionary creation |
| Set comprehension | Concise set creation |
| `*args` | Positional arguments → tuple |
| `**kwargs` | Keyword arguments → dictionary |
| Iterable | Can provide an iterator |
| Iterator | Produces next value and remembers state |
| Generator | Iterator using `yield` |
| `yield` | Produces value and pauses execution |
| Decorator | Adds behavior to another function |
| `@decorator` | Decorator syntax |
| `wraps` | Preserves function metadata |
| Stacked decorators | Multiple decorators around one function |

## ✅ Day 16 Status

- 🟢 List comprehensions
- 🟢 Dictionary comprehensions
- 🟢 Set comprehensions
- 🟢 `*args`
- 🟢 `**kwargs`
- 🟢 Iterators
- 🟢 Generators
- 🟢 Decorators
- 🟢 Decorators with arguments
- 🟢 `functools.wraps`
- 🟢 Stacked decorators
- 🟢 Decorator return-value debugging
- 🟢 Practical employee data-processing assignment

**Engineering takeaway:** Learn → Code → Break → Debug → Understand

## 🚀 Next: Day 17

Python only: **Mutable vs Immutable → References → Object Identity → Shallow Copy → Deep Copy**

NumPy, AI/ML and DSA remain paused until resumed.

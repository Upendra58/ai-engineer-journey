from collections import defaultdict

employees = [
    ("Alice", "IT"),
    ("Bob", "HR"),
    ("Charlie", "IT"),
    ("David", "Finance"),
    ("Eve", "IT")
]
result = defaultdict(list)

for name, department in employees:
    result[department].append(name.upper())

print(result)


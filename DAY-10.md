# Day 10 — Modules, Packages, Imports & JSON

## Focus
Learn how to organize Python code into reusable modules and packages.

## Completed
- Python modules
- `import`
- `from ... import`
- Import aliases
- Custom modules
- Reusable functions
- `__name__ == "__main__"`
- Packages
- `__init__.py`
- Package exports
- JSON serialization/deserialization

## Import Examples
```python
import math
from math import sqrt, pi
import math as m
from math import sqrt as sq
```

## Custom Package
```text
utils/
├── __init__.py
├── number_utils.py
└── string_utils.py
```

Functions included:
- `add`
- `square`
- `largest`
- `is_even`
- `reverse`
- `is_palindrome`
- `count_character`

## Main Entry Point
```python
if __name__ == "__main__":
    print(add(25, 40))
```

## Mini-Project
Built and tested a Student Utility Package using custom modules, package imports, and reusable functions.

## Assessment
**Day 10: 🟢 COMPLETE**

# 📝 Day 15 — NumPy + Pandas Visual Notes

> Goal: Build the Python/data foundation needed for AI/ML.
> Learning flow: Definition → Example → Meaning → Practice

---

# 🔢 PART 1 — NumPy

## 1. What is NumPy?

**Definition:** NumPy (Numerical Python) is a Python library for efficient numerical computation using arrays.

AI/ML commonly represents data as vectors, matrices, and numerical arrays.

```python
import numpy as np

numbers = np.array([5, 10, 15, 20, 25])
```

## 2. NumPy Array

A NumPy array stores values in a structured numerical array.

```python
numbers = np.array([5, 10, 15, 20, 25])

print(numbers)
print(type(numbers))
```

Output:
```text
[ 5 10 15 20 25]
<class 'numpy.ndarray'>
```

## 3. shape, ndim, size

```python
print(numbers.shape)
print(numbers.ndim)
print(numbers.size)
```

Output:
```text
(5,)
1
5
```

| Property | Meaning |
|---|---|
| `shape` | Size of the array along each dimension |
| `ndim` | Number of dimensions |
| `size` | Total number of elements |

Remember:
```text
(5,)  → 5 elements, 1 dimension
(3,3) → 3 rows × 3 columns, 2 dimensions
```

## 4. 2D NumPy Arrays

A 2D array can represent a matrix/table.

```python
data = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
```

Visual:
```text
          column
          0   1   2
row 0 →   5  10  15
row 1 →  20  25  30
row 2 →  35  40  45
```

```python
print(data.shape)  # (3, 3)
print(data.ndim)   # 2
print(data.size)   # 9
```

## 5. NumPy Indexing

**Definition:** Indexing accesses a specific element using its position.

Indexing starts at `0`.

```python
data[row, column]
```

Example:
```python
print(data[1, 2])
```

Output:
```text
30
```

`data[1, 2]` means **2nd row, 3rd column**.

```python
print(data[2, 1])  # 40
```

## 6. NumPy Slicing

**Definition:** Slicing extracts a portion of an array.

General syntax:
```python
array[start:stop]
```

For 2D arrays:
```python
array[row_start:row_stop, column_start:column_stop]
```

### Critical rule
```text
START → inclusive
STOP  → exclusive
```

Example:
```python
numbers = np.array([10, 20, 30, 40, 50])
print(numbers[1:4])
```

Output:
```text
[20 30 40]
```

## 7. 2D Slicing

```python
data[0:2, 0:2]
```

Output:
```text
[[ 5 10]
 [20 25]]
```

Important shape distinction:

```python
data[0, 1:3]      # 1D → [10 15]
data[0:1, 1:3]    # 2D → [[10 15]]

data[:, 2]        # 1D → [15 30 45]
data[:, 2:3]      # 2D → [[15], [30], [45]]
```

**ML lesson:** Shape matters. `(3,)` and `(3,1)` can behave differently in ML operations.

## 8. Vectorized Operations

**Definition:** Vectorization applies an operation to an entire NumPy array without explicitly writing a Python loop.

```python
numbers = np.array([10, 20, 30, 40, 50])

print(numbers + 10)
print(numbers * 2)
print(numbers - 20)
print(numbers / 10)
```

Output:
```text
[20 30 40 50 60]
[ 20  40  60  80 100]
[-10   0  10  20  30]
[1. 2. 3. 4. 5.]
```

## 9. NumPy Aggregation

**Definition:** Aggregation summarizes multiple values.

```python
scores = np.array([70, 85, 90, 65, 80])

print(np.sum(scores))
print(np.mean(scores))
print(np.min(scores))
print(np.max(scores))
```

| Function | Meaning |
|---|---|
| `np.sum()` | Total |
| `np.mean()` | Average |
| `np.min()` | Smallest value |
| `np.max()` | Largest value |

Method style also works:
```python
scores.sum()
scores.mean()
scores.min()
scores.max()
```

## 10. axis in 2D Arrays

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

### axis=0
Works down rows → result per column.

```python
np.sum(data, axis=0)
# [120 150 180]
```

### axis=1
Works across columns → result per row.

```python
np.sum(data, axis=1)
# [ 60 150 240]
```

Mental model:
```text
axis=0 → result per COLUMN
axis=1 → result per ROW
```

## 11. ML-Style NumPy Example

Three students × three subjects:

```python
scores = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])
```

Columns: Math | English | Science

```python
np.sum(scores, axis=1)    # total per student
np.mean(scores, axis=1)   # average per student
np.max(scores, axis=0)    # highest per subject
np.mean(scores)           # overall average
```

---

# 🐼 PART 2 — Pandas

## 12. What is Pandas?

**Definition:** Pandas is a Python library for working with structured/tabular data.

Typical flow:
```text
CSV / Excel / Database / JSON
             ↓
           Pandas
             ↓
         DataFrame
             ↓
      Clean / Filter / Transform
             ↓
             ML
```

### NumPy vs Pandas

| NumPy | Pandas |
|---|---|
| Numerical arrays | Tabular data |
| Arrays / matrices | DataFrame / Series |
| Numerical computation | Data analysis + transformation |
| Great for mathematical operations | Great for real-world datasets |

## 13. DataFrame

**Definition:** A DataFrame is a two-dimensional labelled table of rows and columns.

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Arun"],
    "Age": [25, 28, 24],
    "Salary": [50000, 65000, 45000]
}

df = pd.DataFrame(data)
print(df)
```

Output:
```text
    Name  Age  Salary
0  Rahul   25   50000
1  Priya   28   65000
2   Arun   24   45000
```

The `0, 1, 2` on the left are row indexes.

## 14. Inspecting a DataFrame

```python
print(type(df))
print(df.shape)
print(df.columns)
```

Output:
```text
<class 'pandas.DataFrame'>
(3, 3)
Index(['Name', 'Age', 'Salary'], dtype='str')
```

Meaning:
```text
type(df) → DataFrame
shape    → 3 rows × 3 columns
columns  → Name, Age, Salary
```

## 15. Series vs DataFrame

```python
df["Name"]              # Series
df[["Name", "Age"]]     # DataFrame
```

A single column returns a **Series**. Multiple selected columns return a **DataFrame**.

## 16. Pandas Filtering

**Definition:** Boolean filtering selects rows that satisfy a condition.

```python
df[df["Age"] > 24]
```

Output:
```text
    Name  Age  Salary
0  Rahul   25   50000
1  Priya   28   65000
```

Conceptually:
```python
df["Age"] > 24
```

creates a True/False mask. Pandas keeps rows where the mask is `True`.

## 17. Common Filters

```python
df[df["Salary"] > 50000]
df[df["Age"] == 24]
df[df["Salary"] <= 50000]
```

Operators:
```text
>   greater than
<   less than
>=  greater than or equal
<=  less than or equal
==  equal
```

## 18. Multiple Conditions

### AND → `&`

Both conditions must be true.

```python
df[(df["Age"] > 24) & (df["Salary"] > 50000)]
```

Result:
```text
    Name  Age  Salary
1  Priya   28   65000
```

### OR → `|`

At least one condition must be true.

```python
df[(df["Age"] < 25) | (df["Salary"] > 60000)]
```

Result:
```text
    Name  Age  Salary
1  Priya   28   65000
2   Arun   24   45000
```

### Important rule

Always wrap each condition in parentheses:
```python
(df["Age"] > 24) & (df["Salary"] > 50000)
```

---

# 🐛 Debugging Lesson

A filtering mistake happened when the comparison boundary was changed.

For the intended condition:
```python
df["Age"] < 25
```

`< 25` is different from `<= 25`.

When a filtered result looks wrong:
1. Check the comparison operator.
2. Check each condition separately.
3. Check `&` vs `|`.
4. Check parentheses.
5. Inspect the resulting rows.

---

# 🧠 Day 15 Cheat Sheet

## NumPy
```python
np.array()
array.shape
array.ndim
array.size

array[row, column]
array[start:stop]
array[row_start:row_stop, col_start:col_stop]

array + value
array * value

np.sum()
np.mean()
np.min()
np.max()

np.sum(data, axis=0)  # per column
np.sum(data, axis=1)  # per row
```

## Pandas
```python
pd.DataFrame()

df.shape
df.columns

df["Name"]              # Series
df[["Name", "Age"]]     # DataFrame

df[df["Age"] > 25]

df[(condition1) & (condition2)]  # AND
df[(condition1) | (condition2)]  # OR
```

---

# 🎯 What I Actually Learned Today

## NumPy
- 1D and 2D arrays
- `shape`, `ndim`, `size`
- Indexing
- Slicing
- Start-inclusive / stop-exclusive
- 1D vs 2D slices
- Vectorized operations
- Aggregation
- `axis=0` / `axis=1`
- ML-style numerical data processing

## Pandas
- DataFrame
- Series vs DataFrame
- Selecting columns
- DataFrame shape and columns
- Boolean row filtering
- AND / OR conditions
- Debugging filter boundaries

---

# 🏁 Day 15 Status

**🟢 COMPLETE — NumPy + Pandas Foundations**

Next:
```text
Pandas
  ↓
Create / modify columns
  ↓
Feature engineering basics
  ↓
Missing values
  ↓
Sorting / grouping
  ↓
ML foundations
```

> **Mantra:** Don't just remember the syntax. Understand what the data shape and operation are doing.

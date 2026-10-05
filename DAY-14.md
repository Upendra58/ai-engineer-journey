# 📝 Day 14 — DSA Foundations

> **Status:** 🟢 COMPLETE  
> **Focus:** Arrays, traversal, Big-O, searching, Two Sum, HashMap

## 🎯 What I actually learned

### 1. Arrays / Python Lists as a DSA structure

A data structure organizes and stores data so we can work with it efficiently.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[3])
```

Index access is **O(1)**.

### 2. Array traversal

```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
```

Traversal takes **O(n)** time.

### 3. Find minimum and maximum

```python
numbers = [10, 20, 5, 40, 30]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("smallest:", smallest)
print("largest:", largest)
```

Time: **O(n)**  
Extra space: **O(1)**

### 4. Big-O basics

- Index access → **O(1)**
- Traversal → **O(n)**
- Linear search → **O(n)**
- Update by index → **O(1)**
- Append → **O(1) amortized**
- Insert at the beginning → **O(n)**

Big-O describes how running time or extra memory grows as input size grows.

### 5. Linear search

A linear search checks elements one by one until the target is found.

```python
numbers = [10, 50, 20, 40, 30, 60]
target = 40
found = False

for index in range(len(numbers)):
    if numbers[index] == target:
        found = True
        break

if found:
    print(f"Target {target} found at index {index}")
else:
    print("Not Found")
```

Time: **O(n)** worst case  
Space: **O(1)**

### 6. Important debugging lesson

Putting `print("Not Found")` inside the loop makes it run for every non-matching element.

The final decision belongs **after the search is complete**.

### 7. Two Sum — brute force

Goal: find two numbers whose sum equals the target.

```python
numbers = [2, 7, 11, 15]
target = 9

for number in numbers:
    for num in numbers:
        if number + num == target:
            print(number, num)
```

This brute-force approach uses nested loops: **O(n²)** time.

### 8. HashMap / Python dictionary

A Python `dict` is commonly used as a HashMap.

For Two Sum, store **number → index** so we can quickly check whether the required complement was already seen.

```python
numbers = [3, 8, 4, 6]
target = 10
seen = {}

for i in range(len(numbers)):
    needed = target - numbers[i]

    if needed in seen:
        print(seen[needed], i)
        break

    seen[numbers[i]] = i
```

Output:

```text
2 3
```

Time: **O(n) average**  
Extra space: **O(n)**

### 9. Time vs space trade-off

The HashMap solution uses extra memory to reduce the amount of searching.

> **Use more space to save time.**

## 🧪 Practice completed

- Accessed array elements by index.
- Traversed an array.
- Found minimum and maximum.
- Implemented linear search.
- Debugged incorrect `else` placement.
- Implemented brute-force Two Sum.
- Learned HashMap using Python `dict`.
- Implemented optimized Two Sum with indices.

## ⚠️ Important correction

Frequency counting and most-frequent-element logic were revisited during Day 14, but they were already learned on **Day 6**, so they are **not counted as new Day 14 learning**.

OOP was excluded because it was already completed on Days 7/9.

## 🧠 Key takeaways

1. Understand the data structure before solving the problem.
2. Know the difference between index access and traversal.
3. Keep the final search decision outside the loop when necessary.
4. Nested loops often lead to **O(n²)** solutions.
5. HashMaps can reduce search time to **O(n)** average.
6. Always consider both time and space complexity.

## 🏁 Day 14 result

**DSA foundation started correctly.**

Next: **Day 15 — Two Pointers + Arrays/Hashing practice.**

# Day 6 — Dictionaries & Frequency Counting

## Focus
Learn dictionaries and frequency-counting patterns.

## Completed
- Create/read/update/delete dictionary values
- Key checking
- Dictionary iteration
- `.values()` and `.items()`
- Character frequency
- Word frequency
- Number frequency
- Most-frequent item

## Core Pattern
```python
count = {}

for item in items:
    if item in count:
        count[item] = count[item] + 1
    else:
        count[item] = 1
```

## Practice
Completed character, word, and number frequency problems and found the most frequent item.

Example:
```text
[2, 4, 2, 7, 4, 2, 9, 7, 4, 4]
Most frequent number: 4
Count: 4
```

## Assessment
**Day 6: 🟢 COMPLETE**

### Key Takeaway
Dictionaries are essential for counting, lookup, grouping, and many DSA patterns.

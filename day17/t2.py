from collections import Counter

numbers = [10, 20, 10, 30, 20, 10, 40, 20]
frequency = Counter(numbers)
print(frequency)
print(frequency.most_common(2))

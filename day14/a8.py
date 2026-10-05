numbers = [5, 3, 8, 2, 7]
target = 10

seen = {}  # empty dict

for i in range(len(numbers)):
    needed = target - numbers[i]
    if needed in seen:
        print(seen[needed], i)
        break
    seen[numbers[i]] = i
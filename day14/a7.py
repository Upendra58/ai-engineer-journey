numbers = [3, 8, 4, 6]
target = 10
seen = {}

for i in range(len(numbers)):
    needed = target - numbers[i]

    if needed in seen:
        print(seen[needed],i)
        break
    seen[numbers[i]] = i
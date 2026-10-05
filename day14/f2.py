numbers = [4, 2, 4, 3, 2, 4, 5]
frequency = {}
max_count = 0
most_frequent = None
for number in numbers:
    if number in frequency:
        frequency[number] +=1
    else:
        frequency[number] = 1
    if frequency[number]> max_count:
        max_count = frequency[number]
        most_frequent = number

print(max_count)
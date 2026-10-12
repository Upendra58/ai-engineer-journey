def calculate_average(numbers: list[int])-> float:
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

print(calculate_average([10,20,30]))
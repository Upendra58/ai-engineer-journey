def avg_num(numbers):
    total = 0
    count = 0
    for number  in numbers:
        total = total + number
        count = count + 1
    avg = total / count
    return avg
numbers = [10, 20, 30, 40, 50]
print(avg_num(numbers))
def largest_num(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
numbers = [1,3,5,7,66,33,56,34,33,31,47]
print(largest_num(numbers))

def smallest_num(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
numbers = [10,3,5,7,66,33,56,34,33,2,31,47]
print(smallest_num(numbers))

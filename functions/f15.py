def count_even(number):
    count = 0
    if number % 2==0:
        count = count +1
    return count

def analyse_numbers(numbers):
    counteven= 0
    smallest = numbers[0]
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
        if count_even(number):
            counteven = counteven + 1

    return (largest, smallest, counteven)
numbers = [12, 7, 25, 4, 18, 30, 9]
print(analyse_numbers(numbers))
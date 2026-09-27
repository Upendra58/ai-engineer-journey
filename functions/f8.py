    
def count_even(numbers):
    count = 0
    for number in numbers:
        if number%2 == 0:
            count = count + 1
    return count
numbers = [1,3,5,7,66,33,56,34,33,31,47]
print(count_even(numbers))


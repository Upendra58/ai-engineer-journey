# find both smallest and largest number

numbers = [10, 20, 5, 40, 30]
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print("smallest: ", smallest)
print("largest: ", largest)
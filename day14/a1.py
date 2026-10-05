#find smallest number in a list without using built in funcitons(DSA preparation)

numbers = [10,20,40,1,24]
smallest = numbers[0] # assigning the first element numbers[0] to the smallest
for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)
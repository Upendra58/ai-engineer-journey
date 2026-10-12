def count_numbers():
    for number in range(1,6):
        yield number
numbers = count_numbers()
for number in numbers:
    print(number)
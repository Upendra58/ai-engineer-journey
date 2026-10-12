def count_numbers():
    yield 1
    yield 2

numbers = count_numbers()

print(next(numbers))
print(next(numbers))
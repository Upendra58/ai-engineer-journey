def numbers():
    number = 1

    while True:
        if number % 2 == 0:
            yield number
        number +=1
values = numbers()
for _ in range (10):
    print(next(values))
numbers = [12, 7, 25, 7, 18, 30, 4, 25, 9, 16]
new =[]
count=0
total =0
avg = 0
largest = numbers[0]
secondl = numbers[0]
smallest = numbers[0]
for number in numbers:
    total = total + number
    if number % 2 ==0:
        count= count + 1
    if number not in new:
        new.append(number)
    if number < smallest:
        smallest = number
    if number > largest :
        secondl = largest
        largest = number
    elif number > secondl and number < largest:
        secondl = number
print(total)
print(count)
print(new)
print(largest)
print(secondl)
print(smallest)

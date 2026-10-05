# find if number exists in the array or not

numbers = [10, 50, 20, 40, 30, 60]
found = False

for number in numbers:
    if number == 30:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")
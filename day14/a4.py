# find if number exists in the array or not and print the index of the number

numbers = [10, 50, 20, 40, 30, 60]
target = 400
found = False
for index in range(len(numbers)):
    if numbers[index] == target:
        found = True
        print(f"Target {target} found at index {index} ")
        break
if not found:
    print("Not Found")
numbers = [2, 4, 2, 7, 4, 2, 9, 7, 4, 4]
frequent_number = 0
highest_count = 0
count = {}
for number in numbers:
    if number in count:
        count[number]= count[number] + 1
    else:
        count[number] = 1
    if count[number] > highest_count:
        highest_count = count[number]
        frequent_number = number
for key, value in count.items():
    print(key, ":", value)
print (f"frequent Number: {frequent_number},highest Count: {highest_count}")
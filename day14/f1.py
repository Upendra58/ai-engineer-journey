# Frequency counting : using HASHMAP

numbers = [5, 5, 2, 8, 5, 2]
frequency = {} # empty dict
for number in numbers: # enter the loop
    if number in frequency: # if number in frequency
        frequency[number] += 1 # increase the count by 1
    else: # if number is not in frequency
        frequency[number] = 1 # start the count from 1

print(frequency)
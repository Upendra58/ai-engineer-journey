#find two numbers whose sum is 9 with brute force two sum aprroach

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print (numbers[i], numbers[j])
            print(i, j)

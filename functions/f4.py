def sum_numbers(number):
    count= 0
    for i in range (number+1):
        count = count + i
    return count
number= int(input("enter the number: "))
print(sum_numbers(number))
        
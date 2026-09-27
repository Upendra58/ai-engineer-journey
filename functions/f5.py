def count_even(n):
    count = 0
    for i in range (1,n+1):
        if i%2 == 0:
            count = count + 1
    return count
n= int(input("enter the number: "))
print(count_even(n))
        

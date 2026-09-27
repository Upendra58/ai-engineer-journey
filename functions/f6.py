def sum_even(n):
    sumeven = 0
    i = 1
    while i<=n:
        if i%2 == 0:
            sumeven = sumeven + i
        i += 1
    return sumeven
n= int(input("enter the number: "))
print(sum_even(n))
        

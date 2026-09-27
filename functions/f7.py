def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def count_even(n):
    count = 0
    for i in range (1, n+1):
        if is_even(i):
            count = count + 1
    return count
n= int(input("enter the number: "))
print(count_even(n))


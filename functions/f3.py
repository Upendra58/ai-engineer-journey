def check_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
n= int(input("enter the number: "))
print(check_number(n))
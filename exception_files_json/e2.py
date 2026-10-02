try:
    number = int(input("Enter the number: "))
    result = 100 / number
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("number cannot be zero")
else:
    print (f"the result is {result}")
finally:
    print("Program finished")
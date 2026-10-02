try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Enter a valid number")
else:
    print(f"My age is {age}")
finally:
    print("program finished")
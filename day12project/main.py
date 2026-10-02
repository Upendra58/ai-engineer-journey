from app import calculator
import logging
logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Discount")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "7":
        print("Goodbye!")
        break

    if choice == "1":
        a =int(input("Enter the first number: "))
        b =int(input("Enter the second number: "))
        print("Result:", calculator.add(a, b))
        break

    if choice == "2":
        a =int(input("Enter the first number: "))
        b =int(input("Enter the second number: "))
        print("Result:", calculator.subtract(a, b)) 
        break

    if choice == "3":
        a =int(input("Enter the first number: "))
        b =int(input("Enter the second number: "))
        print("Result:", calculator.multiply(a, b)) 
        break

    if choice == "4":
        a =int(input("Enter the first number: "))
        b =int(input("Enter the second number: "))
        print("Result:", calculator.divide(a, b)) 
        break

    if choice == "5":
        a =int(input("Enter the first number: "))
        b =int(input("Enter the second number: "))
        print("Result:", calculator.percentage(a, b)) 
        break
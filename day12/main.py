from app import calculator
import logging
logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

total = calculator.add(23,45)
print(total)
deficit = calculator.subtract(45,23)
print(deficit)
product = calculator.multiply(23,45)
print(product)
division = calculator.divide(45,5)
print(division)
percent = calculator.percentage(20,200)
print(percent)
print(calculator.divide(3,0))

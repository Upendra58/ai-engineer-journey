#import math_utils  when you want to import whole file
from math_utils import add, square, subtract, maximum, multiply,even, odd


print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))

print("Square: ", square(5))
print("Maximum: ", maximum(20, 15))
print("Is Even: ", even(34))
print("Is odd: ", odd(36))
#print("Is odd: ", math_utils.odd(36)) when you import only math_utils then we call the function with module
# when you import functions from the file then we directly call the function


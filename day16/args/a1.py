# args:
# *args allows a Python function to accept any number of positional arguments and collects those arguments into a tuple inside the function.

#What is args?
#args is simply a variable name commonly used to mean “arguments.”
#In Python, an argument is a value that you pass to a function when calling it.

#Write a function called calculate_sum that uses *args and returns the sum of all numbers passed to it.
#Do not use Python's built-in sum(). Use a loop.
#It should work with different numbers of arguments:

def claculate_sum(*args):
    total = 0
    for number in args:
        total += number
    return total

print(claculate_sum(20,30,40))
print(claculate_sum(34,55,22,44))
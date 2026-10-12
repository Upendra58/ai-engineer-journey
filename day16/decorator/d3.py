from functools import wraps

def my_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Starting calculation")
        result = function(*args, **kwargs)
        print("Calculation Finised")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add.__name__)

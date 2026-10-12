from functools import wraps
def repeat(times):
    def my_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)
        return wrapper
    return my_decorator   

@repeat(5)
def hello():
    print("Hello")

hello()
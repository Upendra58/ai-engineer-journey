def my_decorator(function):
    def wrapper():
        print("Starting function")
        function()
        print("Function finished")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()
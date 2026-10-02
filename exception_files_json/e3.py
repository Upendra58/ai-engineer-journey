def validate_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    else:
        print(f"the age is {age}")  
try:
    validate_age(-8)
except ValueError as error:
    print(error)
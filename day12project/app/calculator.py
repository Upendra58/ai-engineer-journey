import logging

def add(a, b):
    logging.info("Adding two numbers")
    return a+b

def subtract(a, b):
    logging.info("Subtracting two numbers")
    return a - b

def multiply (a , b):
    logging.info("Multiplying two numbers")
    return a * b

def divide(a, b):
    logging.info("Dividing two number")
    if b == 0:
        logging.error("dividing with 0")
        raise ValueError("denominator cannot be 0")
    else:
        return a/b

def percentage(a, b):
    logging.info(f"calculating {a}% of {b}")
    return a/100 * b

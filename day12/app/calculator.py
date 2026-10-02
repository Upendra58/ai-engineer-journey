import logging


def add (a, b):
    logging.info("Adding two numbers")
    return a+b

def subtract(a , b):
    logging.info("Subtracting two numbers")
    return a-b

def multiply(a, b):
    logging.info("Multiplying two numbers")
    return a*b

def divide(a,b):
    logging.info("division of two numbers")
    if b == 0:
        logging.error("Attempted division by zero")
        raise ValueError("denominator cannot be zero")
    else:
        return a/b

def percentage(a , b):
    logging.info(f"Calculating {a}% of {b}")
    return a/100*b
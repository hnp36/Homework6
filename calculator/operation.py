'''Advanced Calculator'''
from decimal import Decimal
def addition(value1:Decimal, value2:Decimal)-> Decimal:
    """adding two numbers"""
    return value1 + value2

def subtraction(value1:Decimal, value2:Decimal)-> Decimal:
    """substracting two numbers"""
    return value1 - value2

def multiplication(value1:Decimal, value2:Decimal)-> Decimal:
    """multipling two numbers"""
    return value1 * value2

def division(value1:Decimal, value2:Decimal)-> Decimal:
    """dividing two numbers and throwing error if divided by 0"""
    if value2 == 0:
        raise ValueError("Cannot divide by zero")
    return value1 / value2

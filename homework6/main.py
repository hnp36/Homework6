"""My calculator3"""
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def calculate_and_print(value1_str, value2_str, operation_key):
    """Perform calculation and print result"""
    operation_lookup = {
        'addition': Calculator.add_numbers,
        'subtraction': Calculator.subtract_numbers,
        'multiplication': Calculator.multiply_numbers,
        'division': Calculator.divide_numbers
    }

    try:
        value1 = Decimal(value1_str)
        value2 = Decimal(value2_str)
        if operation_key not in operation_lookup:
            print(f"Unknown operation: {operation_key}")
            return

        try:
            result = operation_lookup[operation_key](value1, value2)
            print(f"The result of {value1_str} {operation_key} {value2_str} is equal to {result}")
        except ValueError as e:
            print(f"An error occurred: {str(e)}")

    except InvalidOperation:
        print(f"Invalid number input: {value1_str} or {value2_str} is not a valid number.")

def main():
    """main method calling"""
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, value1, value2, operation = sys.argv
    calculate_and_print(value1, value2, operation)

if __name__ == '__main__':
    from calculator.commands import start
    start()

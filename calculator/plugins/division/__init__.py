"""
DivisionCommand Module

This module implements the division operation command for the calculator application."""
# pylint: disable=too-few-public-methods
from decimal import Decimal, InvalidOperation
from calculator.commands.command import Command
from calculator import Calculator

class DivisionCommand(Command):
    """division class"""
    def execute(self):
        """Handles user input for division and performs the operation."""
        try:
            value1 = Decimal(input("Enter first number: "))
            value2 = Decimal(input("Enter second number: "))
            if value2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = Calculator.divide_numbers(value1, value2)
            print(f"Result: {result}")
        except InvalidOperation:  # Catches Decimal conversion errors
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"Unexpected error: {e}")

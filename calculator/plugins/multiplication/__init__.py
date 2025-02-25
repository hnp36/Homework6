"""
MultiplicationCommand Module

This module implements the multiplication operation command for the calculator application."""
# pylint: disable=too-few-public-methods
from decimal import Decimal, InvalidOperation
from calculator.commands.command import Command
from calculator import Calculator

class MultiplicationCommand(Command):
    """Handles user input for multiplication and performs the operation."""
    def execute(self):

        try:
            value1 = Decimal(input("Enter first number: "))
            value2 = Decimal(input("Enter second number: "))
            result = Calculator.multiply_numbers(value1, value2)
            print(f"Result: {result}")
        except InvalidOperation:  # Catches Decimal conversion errors
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"Unexpected error: {e}")

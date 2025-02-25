"""My Calculator"""
from decimal import Decimal
from typing import Callable
from .operation import addition, subtraction, multiplication, division
from .calculation import Calculation
from .calculations import Calculations

class Calculator:
    """Calculator class"""

    @staticmethod
    def execute_operation(value1: Decimal, value2: Decimal,
                         operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(value1, value2, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add_numbers(value1: Decimal, value2: Decimal) -> Decimal:
        """Addition operation"""
        return Calculator.execute_operation(value1, value2, addition)

    @staticmethod
    def subtract_numbers(value1: Decimal, value2: Decimal) -> Decimal:
        """Subtraction operation"""
        return Calculator.execute_operation(value1, value2, subtraction)

    @staticmethod
    def multiply_numbers(value1: Decimal, value2: Decimal) -> Decimal:
        """Multiplication operation"""
        return Calculator.execute_operation(value1, value2, multiplication)

    @staticmethod
    def divide_numbers(value1: Decimal, value2: Decimal) -> Decimal:
        """Division operation"""
        return Calculator.execute_operation(value1, value2, division)

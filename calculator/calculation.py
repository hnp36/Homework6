"""Module for handling arithmetic calculations."""
from decimal import Decimal
from typing import Callable

class Calculation:
    """A class to represent a calculation operation between two decimal values."""

    history = [] # Class-level variable to hold history of calculations

    def __init__(self, value1: Decimal, value2: Decimal,
                 operation: Callable[[Decimal, Decimal], Decimal]):
        """Initialize the calculation with two values and an operation."""
        self.value1 = value1
        self.value2 = value2
        self.operation = operation

    def execute(self) -> Decimal:
        """Execute the stored calculation"""
        return self.perform()

    @staticmethod
    def create(value1: Decimal, value2: Decimal,
               operation: Callable[[Decimal, Decimal], Decimal]):
        """Create a new calculation instance"""
        return Calculation(value1, value2, operation)

    def perform(self) -> Decimal:
        """Execute the calculation"""
        return self.operation(self.value1, self.value2)
    @classmethod
    def clear_history(cls):
        """Clears the calculation history."""
        cls.history = []

    def __repr__(self) -> str:
        """Return string representation of the calculation"""
        return f"Calculation({self.value1}, {self.value2}, {self.operation.__name__[:3]})"

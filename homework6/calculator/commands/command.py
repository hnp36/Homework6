"""Calculator Command Module

Commands:
    - AdditionCommand: Handles addition operations
    - SubtractionCommand: Handles subtraction operations
    - MultiplicationCommand: Handles multiplication operations
    - DivisionCommand: Handles division operations
    - MenuCommand: Displays available calculator operations
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for all commands."""

    @abstractmethod
    def execute(self):
        """Abstract method to be implemented by concrete commands"""

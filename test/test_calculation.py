"""Test module for calculation operations and functionality."""
from decimal import Decimal
import pytest
from calculator.operation import addition, division  # Removed unused imports
from calculator.calculation import Calculation

def test_perform_operations(value1, value2, operation, expected_result):
    """Test calculation operations with different inputs."""
    calculation = Calculation(value1, value2, operation)
    assert calculation.perform() == expected_result

def test_calculation_repr_method():
    """Test string representation of Calculation class."""
    calculation = Calculation(Decimal('15'), Decimal('3'), addition)
    expected_repr = "Calculation(15, 3, add)"
    assert repr(calculation) == expected_repr

def test_division_by_zero_error():
    """Test that division by zero raises appropriate error."""
    calculation = Calculation(Decimal('12'), Decimal('0'), division)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation.perform()

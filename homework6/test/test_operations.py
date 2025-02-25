'''Operations Testing Module'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operation import addition, multiplication, subtraction, division


def test_operation_addition():
    '''Verify addition operation'''    
    calc = Calculation(Decimal('20'), Decimal('5'), addition)
    assert calc.execute() == Decimal('25'), "Add operation failed"

def test_operation_subtraction():
    '''Verify subtraction operation'''    
    calc = Calculation(Decimal('20'), Decimal('5'), subtraction)
    assert calc.execute() == Decimal('15'), "Subtract operation failed"

def test_operation_multiplication():
    '''Verify multiplication operation'''    
    calc = Calculation(Decimal('20'), Decimal('5'), multiplication)
    assert calc.execute() == Decimal('100'), "Multiply operation failed"

def test_operation_division():
    '''Verify division operation'''    
    calc = Calculation(Decimal('20'), Decimal('5'), division)
    assert calc.execute() == Decimal('4'), "Divide operation failed"

def test_division_by_zero():
    """Test that division by zero raises ValueError"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc = Calculation(Decimal('5'), Decimal('0'), division)
        calc.execute()

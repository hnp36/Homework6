'''Advanced Calculator Testing Module'''
from calculator import Calculator

def test_sum():
    '''Verify that the sum function works correctly'''    
    assert Calculator.add_numbers(3, 3) == 6

def test_difference():
    '''Verify that the subtraction function works correctly'''    
    assert Calculator.subtract_numbers(5, 3) == 2

def test_quotient():
    '''Verify that the division function works correctly'''    
    assert Calculator.divide_numbers(10, 2) == 5

def test_product():
    '''Verify that the multiplication function works correctly'''    
    assert Calculator.multiply_numbers(4, 3) == 12

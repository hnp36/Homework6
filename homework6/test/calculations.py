'''My Calculator Test Suite'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation #  no need for 'Calculations'
from calculator.operation import addition, subtraction

@pytest.fixture(name="setup_calculations")
def fixture_setup_calculations():
    """Preparing the calculation history """
    Calculation.clear_history()
    # Add a few sample calculations to the history for testing purposes.
    calc1 = Calculation(Decimal('12'), Decimal('8'), addition)
    calc2 = Calculation(Decimal('30'), Decimal('5'), subtraction)
    Calculation.history.extend([calc1, calc2])
    return [calc1, calc2]

def test_add_calculation_to_history(setup_calculations):
    """Verify that adding a new calculation correctly updates the history."""
    initial_calcs = setup_calculations
    initial_length = len(initial_calcs)
    calc = Calculation(Decimal('3'), Decimal('7'), addition)
    Calculation.history.append(calc)
    assert Calculation.history[-1] == calc
    assert len(Calculation.history) == initial_length + 1

def test_fetch_calculation_history(setup_calculations):
    """Test fetching the calculation history."""
    initial_calcs = setup_calculations
    history = Calculation.history
    assert len(history) == len(initial_calcs)
    assert all(a == b for a, b in zip(history, initial_calcs))

def test_clear_all_calculations(setup_calculations):
    """Test clearing the calculation history."""
    initial_calcs = setup_calculations  # Verify we had calculations initially
    assert len(initial_calcs) > 0
    Calculation.clear_history()
    assert len(Calculation.history) == 0

def test_get_most_recent_calculation(setup_calculations):
    """Test fetching the most recent calculation from history."""
    initial_calcs = setup_calculations
    expected_recent = initial_calcs[-1]  # Last calculation from fixture
    assert Calculation.history[-1] == expected_recent
    assert expected_recent.value1 == Decimal('30')
    assert expected_recent.value2 == Decimal('5')

def test_calculation_with_specific_operation(setup_calculations):
    """Test finding calculations by operation type."""
    initial_calcs = setup_calculations
    assert len(initial_calcs) == 2  # Verify initial state

    add_calcs = [calc for calc in Calculation.history
                 if calc.operation.__name__ == "addition"]
    sub_calcs = [calc for calc in Calculation.history
                 if calc.operation.__name__ == "subtraction"]
    assert len(add_calcs) == 1
    assert len(sub_calcs) == 1
def test_get_latest_calculation_when_empty():
    """Test behavior when getting latest calculation from empty history."""
    Calculation.clear_history()
    assert not Calculation.history

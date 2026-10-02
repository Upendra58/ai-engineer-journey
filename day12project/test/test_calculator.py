from app import calculator
import pytest

def test_add():
    assert calculator.add(3,4)==7
def test_subtract():
    assert calculator.subtract(3,4) == -1

def test_mul():
    assert calculator.multiply(3,4) == 12

def test_percent():
    assert calculator.percentage(20, 200) == 40

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)

def test_divide():
    assert calculator.divide(20, 10 ) == 2

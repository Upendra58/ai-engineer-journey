import pytest
from app import calculator


def test_add():
    assert calculator.add(10, 20) == 30


def test_subtract():
    assert calculator.subtract(20, 10) == 10


def test_multiply():
    assert calculator.multiply(5, 4) == 20


def test_divide():
    assert calculator.divide(20, 5) == 4




def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)

def test_percentage():
    result = calculator.percentage(20, 200)
    assert result == 40
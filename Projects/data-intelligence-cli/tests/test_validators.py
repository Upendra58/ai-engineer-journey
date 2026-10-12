
import pytest

from app.validators import (
    validate_age,
    validate_salary,
    validate_employee,
)


def test_validate_age_converts_string_to_integer():
    assert validate_age("25") == 25


def test_validate_age_rejects_zero():
    with pytest.raises(ValueError):
        validate_age("0")


def test_validate_age_rejects_non_numeric_value():
    with pytest.raises(ValueError):
        validate_age("twenty")


def test_validate_salary_rejects_negative_value():
    with pytest.raises(ValueError):
        validate_salary("-500")


def test_validate_employee_converts_numeric_fields():
    employee = {
        "name": "Alice",
        "age": "25",
        "department": "IT",
        "salary": "50000",
    }

    result = validate_employee(employee)

    assert result["age"] == 25
    assert result["salary"] == 50000

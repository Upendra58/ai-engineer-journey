
from app.analyzer import (
    calculate_total_salary,
    calculate_average_salary,
    highest_paid_employee,
    salary_by_department,
    employee_count_by_department,
    highest_paid_by_department,
)


employees = [
    {"name": "Alice", "age": 25, "department": "IT", "salary": 50000},
    {"name": "Bob", "age": 30, "department": "HR", "salary": 65000},
    {"name": "Charlie", "age": 28, "department": "IT", "salary": 75000},
]


def test_calculate_total_salary():
    assert calculate_total_salary(employees) == 190000


def test_calculate_average_salary():
    assert calculate_average_salary(employees) == 190000 / 3


def test_highest_paid_employee():
    result = highest_paid_employee(employees)
    assert result["name"] == "Charlie"
    assert result["salary"] == 75000


def test_salary_by_department():
    assert salary_by_department(employees) == {
        "IT": 125000,
        "HR": 65000,
    }


def test_employee_count_by_department():
    assert employee_count_by_department(employees) == {
        "IT": 2,
        "HR": 1,
    }


def test_highest_paid_by_department():
    result = highest_paid_by_department(employees)

    assert result["IT"]["name"] == "Charlie"
    assert result["HR"]["name"] == "Bob"

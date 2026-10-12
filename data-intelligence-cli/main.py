
from app.readers import read_csv
from app.validators import validate_employees
from app.reports import print_full_report
from app.analyzer import (
    calculate_total_salary,
    calculate_average_salary,
    highest_paid_employee,
    salary_by_department,
    employee_count_by_department,
    highest_paid_by_department,
)


def main():
    # Step 1: Read employee data from CSV
    employees = read_csv("data/employees.csv")

    # Step 2: Validate employee data
    validated_employees = validate_employees(employees)

    # Step 3: Analyze employee data
    total_salary = calculate_total_salary(validated_employees)
    average_salary = calculate_average_salary(validated_employees)
    highest = highest_paid_employee(validated_employees)
    department_salary = salary_by_department(validated_employees)
    employee_count = employee_count_by_department(validated_employees)
    highest_paid = highest_paid_by_department(validated_employees)

    # Step 4: Generate the complete report
    print_full_report(
        validated_employees,
        total_salary,
        average_salary,
        highest,
        department_salary,
        employee_count,
        highest_paid,
    )


if __name__ == "__main__":
    main()

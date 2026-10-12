def print_header(title):
    print("=" * 40)
    print(title)
    print("=" * 40)

def print_employee_summary(employees, total_salary, average_salary):
    print("\nEmployee Summary")
    print("-" * 40)
    print(f"Total Employees : {len(employees)}")
    print(f"Total Salary    : ₹{total_salary:,.0f}")
    print(f"Average Salary  : ₹{average_salary:,.0f}")

def print_department_salary_report(department_salary):
    print("\nSalary by Department")
    print("-" * 40)

    for department, salary in department_salary.items():
        print(f"{department:<15}: ₹{salary:,.0f}")

def print_employee_count_report(department_count):
    print("\nEmployee Count by Department")
    print("-" * 40)

    for department, count in department_count.items():
        print(f"{department:<15}: {count}")

def print_highest_paid_by_department_report(highest_paid):
    print("\nHighest-Paid Employee by Department")
    print("-" * 40)

    for department, employee in highest_paid.items():
        print(
            f"{department:<15}: "
            f"{employee['name']} "
            f"(₹{employee['salary']:,.0f})"
        )
        
def print_highest_paid_employee_report(employee):
    print("\nHighest-Paid Employee")
    print("-" * 40)
    print(f"Name       : {employee['name']}")
    print(f"Department : {employee['department']}")
    print(f"Salary     : ₹{employee['salary']:,.0f}")

def print_full_report(
    employees,
    total_salary,
    average_salary,
    highest_employee,
    department_salary,
    department_count,
    highest_by_department,
):
    print_header("DATA INTELLIGENCE REPORT")

    print_employee_summary(
        employees,
        total_salary,
        average_salary,
    )

    print_highest_paid_employee_report(highest_employee)

    print_department_salary_report(department_salary)

    print_employee_count_report(department_count)

    print_highest_paid_by_department_report(highest_by_department)
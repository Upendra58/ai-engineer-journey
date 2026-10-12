def calculate_total_salary(employees):
    total = 0
    for employee in employees:
        total += employee["salary"]
    return total

def calculate_average_salary(employees):
    if not employees:
        raise ValueError("Employee list cannot be empty")

    total_salary = calculate_total_salary(employees)
    average_salary = total_salary / len(employees)

    return average_salary


def highest_paid_employee(employees):
    if not employees:
        raise ValueError("Employee list cannot be empty")
    highest_employee = employees[0]
    for employee in employees:
        if employee["salary"] > highest_employee["salary"]:
            highest_employee = employee
    return highest_employee

def salary_by_department(employees):
    department_salary = {}

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        if department not in department_salary:
            department_salary[department] = 0

        department_salary[department] += salary

    return department_salary

def employee_count_by_department(employees):
    department_count = {}

    for employee in employees:
        department = employee["department"]

        if department not in department_count:
            department_count[department] = 0

        department_count[department] += 1

    return department_count

def highest_paid_by_department(employees):
    highest_paid = {}

    for employee in employees:
        department = employee["department"]

        if department not in highest_paid:
            highest_paid[department] = employee

        else:
            if employee["salary"] > highest_paid[department]["salary"]:
                highest_paid[department] = employee

    return highest_paid
    
    

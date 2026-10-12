def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a valid integer")

    if age <= 0:
        raise ValueError("Age must be greater than 0")

    if age > 100:
        raise ValueError("Age must be 100 or less")

    return age


def validate_salary(salary):
    try:
        salary = int(salary)
    except ValueError:
        raise ValueError("Salary must be a valid integer")

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    return salary


def validate_required_fields(employee):
    required_fields = ["name", "age", "department", "salary"]

    for field in required_fields:
        if field not in employee:
            raise ValueError(f"Required field is missing: {field}")

    return employee


def validate_non_empty_fields(employee):
    fields = ["name", "department"]

    for field in fields:
        if not employee[field].strip():
            raise ValueError(f"{field} cannot be empty")

    return employee


def validate_employee(employee):
    validate_required_fields(employee)
    validate_non_empty_fields(employee)

    employee["age"] = validate_age(employee["age"])
    employee["salary"] = validate_salary(employee["salary"])

    return employee


def validate_employees(employees):
    validated_employees = []

    for employee in employees:
        validated_employee = validate_employee(employee)
        validated_employees.append(validated_employee)

    return validated_employees


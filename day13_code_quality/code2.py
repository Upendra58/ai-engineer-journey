def calculate_salary(salary: float, bonus: float)-> float:
    bonus_amount = salary * bonus/100
    final_salary = salary + bonus_amount
    return final_salary

salary = 50000
bonus = 10

final_salary = calculate_salary(salary,bonus)
print(final_salary)
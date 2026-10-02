class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
    def work(self):
        print("Employee working")
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def work(self):
        print("Writing Code")
class Tester(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def work(self):
        print("Testing Code")
employees = [
    Developer("Upendra", 50000),
    Tester("Rahul", 45000),
    Employee("John", 40000)
]

for employee in employees:
    employee.work()


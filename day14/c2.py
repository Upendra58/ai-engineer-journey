class Employee:
    company = "Wipro"
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"{self.name} - {self.company} - {self.salary}")

    def give_raise(self,amount):
        self.salary += amount
    
    def is_high_earner(self):
        return self.salary >= 50000
    
emp1 = Employee("Upendra",5000)

emp1.display_info()

emp1.give_raise(5000)
emp1.display_info()
print(emp1.is_high_earner())
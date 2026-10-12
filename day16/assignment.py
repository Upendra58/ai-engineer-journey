from functools import wraps
employees = [
    {"name": "Alice", "age": 25, "salary": 50000, "department": "IT"},
    {"name": "Bob", "age": 30, "salary": 65000, "department": "HR"},
    {"name": "Charlie", "age": 28, "salary": 75000, "department": "IT"},
    {"name": "David", "age": 24, "salary": 45000, "department": "Finance"},
    {"name": "Eve", "age": 32, "salary": 80000, "department": "IT"},
]
iterator = iter(employees)

#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

#generator
def employee_generator(employees):
   for employee in employees:
    yield employee
employees_gen = employee_generator(employees)
print(next(employees_gen))
print(next(employees_gen))
print(next(employees_gen))


#Create a list containing the names of employees whose salary is greater than 60000.
salary_g = [employee["name"] for employee in employees if employee["salary"] > 60000]
print(salary_g)
# create a dictionary containing the names and salary 
dict_s = {employee["name"] : employee["salary"] for employee in employees}
print(dict_s)
#set comprehension Create a set containing all unique departments.
set_s = {employee["department"] for employee in employees}
print(set_s)

#It should accept any number of salaries.
def calculate_salary(*args):
    total_salary = 0
    for number in args:
        total_salary += number
    return total_salary

print(calculate_salary(50000, 65000, 75000))

#should display each key and value.
def show_employee(**kwargs):
    for key,value in kwargs.items():
        print(key,":" , value)
    
show_employee(
    name="Upendra",
    age=26,
    role="AI Engineer"
)


#decorator create avg_salary

def my_decorator(function):
   def wrapper(*args, **kwargs):
    print("calculation started")
    result = function(*args, **kwargs)
    print("average calculation done")
    return result
   return wrapper

@my_decorator
def calculate_average(*args, **kwargs):
   average = 0
   total = 0
   for number in args:
        total += number
   average = total/len(args)
   return average

print(calculate_average(30,20,10))


def log_function(function):
   @wraps(function)
   def wrapper1(*args, **kwargs):
      print("started")
      result1 = function(*args,**kwargs)
      print("completed")
      return result1
   return wrapper1

@log_function
def add(a,b):
   return a+b

print(add.__name__)

#decorator repeat

def repeat(times):
   def time_decorator(function):
      @wraps(function)
      def wrapper2(*args, **kwargs):
         for _ in range(times):
            result3 = function(*args, **kwargs)
         return result3

      return wrapper2
   return time_decorator

@repeat(3)
def greet():
   print("Processing Employees...")

greet()

# final combination
#The most important part is combining the decorators:
#The function should return the names of employees whose salary is at least minimum_salary.
@repeat(2)
@log_function
def show_high_salary_employees(employees, min_salary = 60000):
   high_salary = [
    employee["name"] for employee in employees if employee["salary"] >= min_salary
   ]
   return high_salary

print(show_high_salary_employees(employees))




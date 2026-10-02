class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old")
student1 = Student("Upendra",25)
student2 = Student("Rahul",23)

student1.introduce()
student2.introduce()


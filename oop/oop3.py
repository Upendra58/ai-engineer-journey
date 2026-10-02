class Student:
    school = "ABC School"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old and from {self.school}")

student1 = Student("Upendra",26)
student2 = Student("Rahul",23)

student1.introduce()
student2.introduce()

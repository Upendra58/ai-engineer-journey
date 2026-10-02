class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def show_result(self):
        if self.marks >= 40:
            print(f"{self.name} passed with {self.marks} marks")
        else:
            print(f"{self.name} failed with {self.marks} marks")
student1 = Student("upendra", 26, 78)
student2 = Student ("Rahul",26,32)

student1.show_result()
student2.show_result()
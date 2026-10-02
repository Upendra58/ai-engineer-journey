class Student:
    def __init__(self, marks):
        self.__marks = marks
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self, value):
        if value >= 0 and value <=100:
           self.__marks = value
        else:
            print("Marks cannot be less than 0 and greater than 100")

student = Student(80)

print(student.marks)

student.marks = 900

print(student.marks)
class Student:
    def __init__(self, name="unknown", age="unknown", grade="unknown"):
        self.name = name
        self.age = age
        self.grade = grade

    def studentInfo(self):
        print(f'{self.name} is of {self.age} years old and has scorerd {self.grade} grade')


student1 = Student("Ram", 12, "A+")
student2 = Student("Laxman", 10, "A")
student3 = Student()

student1.studentInfo()
student2.studentInfo()
student3.studentInfo()
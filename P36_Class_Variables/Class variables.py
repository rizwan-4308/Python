
class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 25)
student3 = Student("Mary", 30)
student4 = Student("John", 35)

""" 
print(student1.name)
print(student1.age)
print(student1.class_year)
"""

""" 
print(student2.name)
print(student2.age)
print(Student.class_year)
"""

# print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)



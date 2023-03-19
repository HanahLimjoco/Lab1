import random

class Student:
    def __init__(self, name, age, id_num):
        self.name = name
        self.age = age
        self.id_num = id_num
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id_num}"

students = [
    Student("Alice", 20, "001"),
    Student("Bob", 22, "002"),
    Student("Charlie", 21, "003"),
    Student("Dave", 19, "004"),
]

# Shuffle the list of students
random.shuffle(students)

# Sort the list of students by age
students.sort(key=lambda x: x.name)

# Display all attributes of the sorted list of students
for student in students:
    print(student)
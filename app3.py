from models.classroom import Classroom
from models.student import Student


oop = Classroom("OOP")
oop.add_student(Student(1, "Alice", 20, 123456))
oop.add_student(Student(2, "Bob", 22, 234567))
print(f'{oop.name} has {len(oop)} students:')
oop.add_student(Student(3, "Charlie", 21, 345678))
print(len(oop))
for i in range(len(oop)):
    print(oop[i])
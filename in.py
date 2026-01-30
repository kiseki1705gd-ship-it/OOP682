class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def info(self):  
        print(f"Student Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

class Staff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id

    def info(self):   # override (Polymorphism)
        print(f"Staff Name: {self.name}, Age: {self.age}, ID: {self.staff_id}")

def main():
    people = [
        Student("Alice", 20, 123456),
        Staff("Bob", 45, 987654),
        Student("Charlie", 22, 2431465)
    ]

    for person in people:
        person.info()    

if __name__ == "__main__":
    main()

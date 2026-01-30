from models.person import Person

class Staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)

    def __str__(self):
        return f"Staff(ID): {self.pid}, ชื่อ: {self.name}, อายุ: {self.age}, รหัสพนักงาน: {self.staff_id})"
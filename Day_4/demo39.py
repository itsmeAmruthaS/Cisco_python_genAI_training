
class Teacher:
    def __init__(self, name, subject):
        self.name = name

    def teach(self):
        print(self.name, " is teaching")

class Dept:
    def __init__(self, teacher):
        self.teacher = teacher


teacher1 = Teacher("Alice")
dept1 = Dept(teacher1)
dept1.teacher.teach()


#Composition
class Engine:
    def start(self):
        return "Engine Starting"

class Car:
    def __init__(self,name):
        self.name = name
        self.engine = Engine()
    def start(self):
        return f"{self.engine.start()}"
car1 = Car("ferrari")
c = car1.start()
print(c)

#Aggregation
class Student:
    def __init__(self,name):
        self.name = name
class Department:
    def __init__(self,name):
        self.name = name
        self.students = []
    def add_students(self,student):
        return self.students.append(student)
s1 = Student("Ali")
s2 = Student("John")

d = Department("Computer Science")
d.add_students(s1)
d.add_students(s2)
print([student.name for student in d.students])
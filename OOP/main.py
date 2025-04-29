"""class Person:
    def __init__(self, name):
        self.name = name
        print (f"Person intialized with me: {self.name}")
class Employee(Person):
    def __init__(self, name, employee_id):
        super(Employee, self).__init__(name)
        self.employee_id = employee_id
        print (f"Employee intialized with name: {name} and ID: {employee_id}")

class Teacher(Employee,Person):
    def __init__(self, name, teacher_id):
        super(Teacher, self).__init__(name, teacher_id)
        print (f"Teacher intialized with name: {name} and ID: {teacher_id}")

x=Teacher("omar","q582")"""




class Human:
    def eat(self):
        print("human eats")


class Mammal:
    def eat(self):
        print("mammal eats")

class Employee(Human,Mammal):
    pass

E = Employee()
E.eat()

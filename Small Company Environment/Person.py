class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep (self,hours):
         if hours == 7:
            print ('Happy')
         elif hours < 7:
             print ('Tired')
         else:
             print ('Lazy')

    def eat(self,meals):
        if meals ==3:
            print ('100% Healthy')
        elif meals ==2:
            print ('75% Healthy')
        elif meals ==1:
            print ('50% Healthy')

    def buy(self,items):
        cost = items*10
        if self.money >= cost:
            self.money -= cost
        else:
            print ('Not enough money to buy')

class Employee(Person):
    def __init__(self,*args,car,email,id,salary,distanceToWork):
        super().__init__(*args)
        self.id=id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self,hours):
        if hours == 8:
            print ('Happy')
        elif hours < 8:
            print ('Lazy')
        else:
            print ('Tired')

    def drive(self,distanceToWork):
        self.car.run(self.car.velocity,distanceToWork)


    def refuel(self,gasAmount=100):
        self.car.fuelRate += gasAmount
        if self.car.fuelRate > 100:
            self.car.fuelRate = 100


class Car:
    def __init__(self,name,fuelRate,velocity):
        self.name = name
        self.fuelRate = min(max(fuelRate,0),100)
        self.velocity = min(max(velocity,0),200)

    def run(self,velocity,distance):
        self.velocity = min(max(velocity,0),200)
        fuel_needed = distance
        if self.fuelRate > fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            distance_possible= self.fuelRate
            remaining = distance - distance_possible
            self.fuelRate =0
            self.stop(remaining)

    def stop(self,remaining):
        self.velocity = 0
        if remaining >0:
            print(f"Out of Fuel, {remaining} km left to go ")
        else:
            print("Arrived at destination")









class Office:
    empNum=0
    def __init__(self,name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self,emplid):
        for emp in self.employees:
            if emp.id == emplid:
                return emp
        return None

    def hire(self,employee):
        self.employees.append(employee)
        Office.empNum+=1
        print(f"Employee {employee.name} has been hired.")


    def fire(self,emplid):
        emp=self.get_employee(emplid)
        if emp:
            self.employees.remove(emp)
            Office.empNum-=1
            print (f"Employee{emplid} has been fired")
            return emp
        else:
            print (f"No employee with ID: {emplid} has been found")

        return None


    def deduct(self,emplid,deduction):
         emp=self.get_employee(emplid)
         if emp:
             emp.salary-=deduction
             print(f"{deduction} l.e deducted from {emp.name}")
             return emp
         else:
             print("Employee not found")
         return None
    def reward (self,emplid,reward):
         emp=self.get_employee(emplid)
         if emp:
             emp.salary += reward
             print(f"{reward} l.e rewarded to {emp.name}")

    def check_lateness(self,emplid,moveHour):
        emp=self.get_employee(emplid)
        if emp:
            late=Office.calcualte_lateness(9,moveHour,emp.distanceToWork,emp.car.velocity)
            if late:
                self.deduct(emplid,10)
            else:
                self.reward(emplid,10)

    @staticmethod
    def calcualte_lateness(targetHour,moveHour,distance,velocity):
        if velocity ==0:
            return True
        arrival_time = moveHour+(distance/velocity)
        return arrival_time > targetHour
    @classmethod
    def change_emps_num(cls,num):
        cls.empNum = num




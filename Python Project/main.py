from Person import Person
from Person import Car
from Person import Employee
from Person import Office

samy_car= Car("fiat128", fuelRate=100, velocity=60)
samy= Employee("samy", 500,"Neutral",100,car=samy_car,email="Samy@gmail.com",id=1,salary=3000,distanceToWork=20)
iti_office= Office("ITI Smart Village")
iti_office.hire(samy)
samy.drive(samy.distanceToWork)
iti_office.check_lateness(emplid=1,moveHour=7.5)
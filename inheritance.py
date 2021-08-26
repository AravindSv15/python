class Vehicle:
    def general_usage(self):
        print("general usage is transport")
class Car(Vehicle):
    def __init__(self):
        print("iam a car")
        self.wheels=4
        self.has_roof=True
    def specific_usage(self):
        print("specific usage : commute to work, vacation with family")

class Bike(Vehicle):
    def __init__(self):
        print("iam a bike")
        self.wheels=2
        self.has_roof=False
    def specific_usage(self):
        print("specific usage : racing")

c=Car()
c.general_usage()
c.specific_usage()

b=Bike()
b.general_usage()
b.specific_usage()
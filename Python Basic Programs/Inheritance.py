class Car:
    print("This is the Parent Class.")
    
class Bike:
    print("This is Child Class.")
    
class Truck(Car,Bike):
    print("This is Child of Child class.")
    
o = Truck()

        
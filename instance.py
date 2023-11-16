class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")
        
car_instance = Car()
motorcycle_instance = Motorcycle()


car_instance.start_engine()         
motorcycle_instance.start_engine()  


class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class Pickup(Vehicle):
    pass;

class Van(Vehicle):
    pass;

class Estatecar(Vehicle):
    pass;

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

pickup1 = Pickup()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estate1 = Estatecar()
estate1.turnOnAirConditioner()

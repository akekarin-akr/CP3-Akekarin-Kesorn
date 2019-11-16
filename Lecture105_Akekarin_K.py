class Vehicle:
    licenseNumber = ""
    serialCode = ""
    def turnOnAircoditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    def sayHello(self):
        print("Hello World")
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

C = Car()
C.turnOnAircoditioner()

P = PickUp()
P.turnOnAircoditioner()

V = Van()
V.turnOnAircoditioner()

E = Estatecar()
E.turnOnAircoditioner()






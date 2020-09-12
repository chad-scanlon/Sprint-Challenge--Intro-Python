# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
class Vehicle:      #Base Class
    # def __init__(self):
    pass

class GroundVehicle(Vehicle):     #SubClass
    # def __init__(self):
    # super().__init__()
    pass
    

class Car(GroundVehicle):   #SubSubClass
    # def __init__(self):
    # super().__init__()
    pass
class Motorcycle(GroundVehicle):    #SubSubClass
    # def __init__(self):
    # super().__init__()
    pass

class FlightVehicle:      #Base Class
    # def __init__(self):
    pass

class Airplane(FlightVehicle):      #SubClass
    # def __init__(self):
    pass

class Starship:      #Base Class
    # def __init__(self):
    pass
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

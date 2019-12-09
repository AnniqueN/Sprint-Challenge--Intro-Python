# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class is Vehicle:

#base (parent) class
class Vehicle:
    pass

#FlightVehicle class, subclass of Vehicle
class FlightVehicle(Vehicle):
    pass

#Starship class, subclass of FlightVehicle
class Starship(FlightVehicle):
    pass

#GroundVehicle class, subclass of Vehicle
class GroundVehicle(Vehicle):
    pass

#Airplane class, subclass of Flightvehicle
class Airplane(FlightVehicle):
    pass

#Car class, subclass of GroundVehicle
class Car(GroundVehicle):
    pass

#Motorcycle class, subclass of GroundVehicle
class Motorcycle(GroundVehicle):
    pass
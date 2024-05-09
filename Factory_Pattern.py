"""
Simple explanation way:
    This is like having a special Lego machine. You tell it what kind of thing you want to build
    (a car, spaceship, etc.),and it pops out all the bricks you need, ready to snap together!

Advanced Way:
    Factory Method is a Creational Design Pattern that allows an interface or a class to create an object,
    but lets subclasses decide which class or object to instantiate.
"""

class FirstClass:
    def __init__(self) :
        self.reserv_degree="Welcome to the First class Degree! Wish you a nice trip free of fatigue with our airline :) "

class BusinessClass:
    def __init__(self) :
        self.reserv_degree="Welcome to the Business class Degree! Have a nice trip! "

class EconomyClass:
    def __init__(self) :
        self.reserv_degree="Welcome to the Economy Degree!"


class Decision_Maker:                  #Factory
    @staticmethod
    def options(choice) :
        try:
            if choice=="F":
                return FirstClass()
            elif choice=="B":
                return BusinessClass()
            elif choice=="E":
                return EconomyClass()
        except AttributeError:
            print("Invalid Option")
        

# Testing the decision maker
Client_Descision=Decision_Maker.options("E")
print(Client_Descision.reserv_degree)

 


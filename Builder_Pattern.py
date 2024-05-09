"""
Simple explained way:
    It is like having an instruction sheet for a really complicated Lego model. It tells you exactly which bricks
    to use and how to put them together step-by-step.

Advanced way: 
    It is a creational design pattern in object-oriented programming. Its purpose is to separate the construction of a
    complex object from its representation. This separation allows for more control over the construction process
    and better flexibility in creating different variations of the complex object.

"""

# class SpaceshipBuilder:
#     def __init__(self):
#         self.route = None
#         self.payload = None
#         self.spare_fuel = None

#     def set_route(self, route):
#         self.route = route
#         return self

#     def set_payload(self, payload):
#         self.payload = payload
#         return self

#     def set_spare_fuel(self, spare_fuel):
#         self.spare_fuel = spare_fuel
#         return self

#     def build(self):
#         if not all([self.route, self.payload, self.spare_fuel]):
#             raise Exception("Be Careful! Missing spaceship parts!")
#         return Spaceship(self.route, self.payload, self.spare_fuel)

# class Spaceship:
#     def __init__(self, route, payload, spare_fuel):
#         self.route = route
#         self.payload = payload
#         self.spare_fuel = spare_fuel

#     def launch(self):
#         print(f"The spaceship current route is: {self.route}\n  With a max payload: {self.payload} Ton \n  Having spare fuel of: {self.spare_fuel} (L) is launching!")

# spaceship_builder = SpaceshipBuilder()
# spaceship = spaceship_builder.set_route("Mars") \
#                              .set_payload(float(2.75)) \
#                              .set_spare_fuel(int(4450)) \
#                              .build()
# spaceship.launch()  




















"""
Simple explanation way:
    This is like having only one really special Lego brick in the whole world.
    Everyone can use it in their builds, but there's only one! 
    
Advanced way:
    Singleton Method is a type of Creational Design pattern that makes sure that only one instance 
   of a class exists.
"""

import copy
class Singleton_Pattern:
    _instance=["Khaled",20,"MSA"]
    def __new__(cls):
        # return cls  # Will return class reference for all objects
        return object.__new__(cls)   # objects will have its own reference
    
    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"
    
    @classmethod
    def class_method(cls):
        print("Using Class method")
        return cls._instance
     

obj=Singleton_Pattern()
print(obj.class_method())


print(f"id(Singleton)\t= {id(Singleton_Pattern)}")

OBJECT1 = Singleton_Pattern()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)        # even if we take a copy from other objects,same id will be produced
print(f"id(OBJECT2)\t= {id(OBJECT2)}")  

OBJECT3 = Singleton_Pattern()
print(f"id(OBJECT3)\t= {id(OBJECT3)}") 



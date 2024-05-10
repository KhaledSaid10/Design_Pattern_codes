"""
FlyWeight is a type of Structural Pattern taht allows sharing of a large 
number of objects in a minized memoryu usage
"""

class Insects():
    def __init__(self):
        pass
    def insect_name(self):
        print(f"The fly is: {self.fly}")

class insect_environment(Insects):
    insect_dict={}
    def __new__(cls, name, insect_family):
        try:
            obj=cls.insect_dict[insect_family]
        except KeyError:  
            obj=object.__new__(cls)
            cls.insect_dict[insect_family]=obj
        return obj
        
    def set_insectinfo(self,insectinfo):
         Fly1=Insects()
         self.insectinfo=Fly1.insect_name(insectinfo)

    def get_insectinfo(self):
        return (self.insectinfo)

if __name__ == "__main__":

    data = (("M","Mosquito" , 1) , ("A","Ants" , 2) , ("F","Flies" , 1))
    insect_family_object = []

    for i in data:
        obj = insect_environment(i[0],i[1])
        obj.set_insectinfo(i[0])
        insect_family_object.append(obj)

    """similar id's says that they are same objects """


    for i in insect_family_object:
        print("id = " + str(id(i)))
        print(i.get_insectinfo())
		  








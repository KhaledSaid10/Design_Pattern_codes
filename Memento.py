"""
The Memento Design Pattern is a behavioral design pattern that allows you to save and restore the previous state of
an object without revealing the details of its implementation.
It is particularly useful for features like undo or rollback capabilities in applications.
"""

import copy
class Memento:
    def __init__(self,state) :
        self.state=copy.deepcopy(state)

    def get_state(self):
        return self.state

class Originator:
    def __init__(self) :
        self.state=None
    
    def set_state(self,state):
        self.state=state
    
    def get_state(self):
        return self.state

    def save_to_memento(self):
        return Memento(self.state)
    
    def restore_from_memento(self,memento):
        self.state=memento.get_state()
    
class Caretaker:
    
    def __init__(self) -> None:
        self._mementos=[]

    def add_to_mementos(self,memento):
        self._mementos.append(memento)
    
    def get_from_memento(self,index):
        return self._mementos[index]

if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()
    originator.set_state("State #1")
    originator.set_state("State #2")
    caretaker.add_to_mementos(originator.save_to_memento())

    originator.set_state("State #3")
    caretaker.add_to_mementos(originator.save_to_memento())

    originator.set_state("State #4")
    print(f"Current State: {originator.get_state()}")

    originator.restore_from_memento(caretaker.get_from_memento(0))
    print(f"First saved State: {originator.get_state()}")
    originator.restore_from_memento(caretaker.get_from_memento(1))
    print(f"Second saved State: {originator.get_state()}")


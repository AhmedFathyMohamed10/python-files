from abc import ABC, abstractmethod

class Body(ABC):
    @abstractmethod
    def set_name(self):
        pass

    @abstractmethod
    def set_age(self):
        pass


class Human(Body):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self):
        return self.__name
    
    def set_age(self):
        return self.__age
    
if __name__ == '__main__':
    name, age = 'Ahmed', 23

    obj1 = Human(name, age)
    obj1.name = 'Mahmoud'
    obj1.__age = 89

    print(obj1.set_name(), ' ', obj1.set_age())


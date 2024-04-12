class People:
    count = 0

    def __init__(self, name):
        self.name = name
        People.count += 1

    @classmethod
    def count_instance(cls):
        return cls.count
    
# print('Count: ', People.count_instance())
person1 = People('Alice')
person1 = People('Alice')
person1 = People('Alice')
person1 = People('Alice')
person1 = People('Alice')
print('Count of Instances: ', People.count_instance())

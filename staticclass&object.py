class animal:
    def __init__(self, value):
        self.value = value

    def printVal(self, val):
        self.value = val

    @staticmethod
    def add(a,b):
        return a+b  


a = animal(10)
print(a.value)
a.printVal(11)      
print(a.value)
#static method called by object as well from class name
print(a.add(5,9))
print(animal.add(5,9))

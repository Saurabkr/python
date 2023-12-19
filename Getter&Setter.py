class Getter_setter:
    def __init__(self, a, b):
        self.a = a 
        self.b = b

    def sum(self):
        return self.a+self.b
    
    @property
    def multiply(self):
        if self.a == None or self.b == None:
            print("Value is not set by setter")
            return 0
        return self.a*self.b
    
#setter to set the value
    @multiply.setter
    def multiply(self, nValue):
        self.a = nValue*self.a
        self.b = nValue*self.b

#use to delete the set value by setter
    @multiply.deleter
    def multiply(self):
        self.a = None
        self.b = None


a = Getter_setter(10,5)
print(a.sum())

a.multiply = 10
print(a.multiply)

del a.multiply
print(a.multiply)

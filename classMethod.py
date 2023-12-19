#class Methos is use to change the variable inside the class

class emp:
    cmpyName = "Apple"
    # def __init__(self,cmpyName, empName):
    #     self.cmpyName = cmpyName
    #     self.empName = empName

    def info(self):
        print(f"{self.empName} is working in {self.cmpyName}")
    
    @classmethod
    def changeCmpyName(cls, nCmpy):
        cls.cmpyName = nCmpy    


c = emp()
c.empName = "saurab"
c.info()
print(c.cmpyName)
c.changeCmpyName("Tesla")
print(c.cmpyName)
print(emp.cmpyName)


class person:
    def __init__(self):
        print("Hi i am default constructor")

    def fun(self):
        print("i am function of person class")   


a = person() 
a.fun()    

class car:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def feature(self):
        print(f'ferrai achieve upto {self.speed} and has capacity of {self.capacity}')    


b = car(160, 200)   
b.feature()     
        


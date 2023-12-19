class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    #there are  __add__ dunder method which use to add two object(called in background) then it got overloaded
    def __add__(self,x):
        return f"{self.i+ x.i}i+ {self.j+ x.j}j+ {self.k+ x.k}k"

val = Vector(2,4,5)
val1 = Vector(2,7,5)   
print(val+val1)
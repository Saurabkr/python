class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    #if there are any __add__ operator then it got overloaded
    def __add__(self,x):
        return f"{self.i+ x.i}i+ {self.j+ x.j}j+ {self.k+ x.k}k"

val = Vector(2,4,5)
val1 = Vector(2,7,5)   
print(val+val1)

#lambda function format
sqr = lambda x: x*x
avg = lambda x,y,z: (x+y+z)/3

print(sqr(5))

#use to call fuction inside function
def fun(sqr,value):
    return 5 + sqr(value)

print(fun(sqr,5))
print(avg(3,5,10))

#or
print(fun(lambda x: x*x,5))


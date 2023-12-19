def comparison(a,b):
    if(a>b):
        print("First number is greater")
    elif(a==b):
        print("Both numbers are equal")
    else:
        print("Second Number is greater")

def even(x):
    if(x%2==0):
        print("Number is even")
    else:
        print("Number is odd")    

def calculation(a,b,c):
    pass             

# x = int(input("enter first number : "))
# y = int(input("enter second number : "))
x=10
y=90
comparison(x,y)
even(x)
   

c = 10
d = 1
comparison(c,d)
even(c)

#function arguments

def nrmlFunc(a='saurab',b='man'):
    print(a,"is a good",b)

#list is passed as argument
def avg(*numbers):
    sum = 0
    for i in numbers:
        sum+=i
    aveg = sum/len(numbers)
    return aveg    

nrmlFunc(b='person',a='aman')    
average = avg(2,3,4)


#dictionary is passed as argument

def name(**names):
    print("my name is", names["fname"], names["lname"])


name(fname="saurab", lname="kumar")
print(average)
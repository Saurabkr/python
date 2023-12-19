#Decorator
def greet(fn):
    def wishes():
        print("Hi, Good Morning!")
        fn()
        print("Thank you,Byee.")
    return wishes    


@greet
def msg():
    print("How can i help you?")


msg()

#Example 2

def sum(fn):
    def addition(*args, **quargs):
        print("Perform addition")
        fn(*args, **quargs)
        print("Thank you")
    return addition

@sum
def add(a,b):
    res = a+b
    print(f"Sum of two number is {res}")

add(3,9)    
    

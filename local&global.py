x = 10
print(x)

def func():
    
    global x
    x = 1

#we can change global variable value from inside the fubction    
func()
print(x)    

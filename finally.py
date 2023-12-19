l = [1,2,3]
def func():
    try:
        inp = int(input("Enter index: "))
        print(l[inp])
        #First finally block will run then function returns its value
        return 1

    except:
       return 0
    
    finally:
       print("I will always run")    

x=func()
print(x)
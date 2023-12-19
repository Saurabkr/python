number = int(input("Enter a number : "))

match number:
    case 0:
        print("number is equal to zero")
    #default cases:
    case _ if(number>0): 
        print("number is greater than zero")    
    case _ if(number<0):
        print("number is less than zero")
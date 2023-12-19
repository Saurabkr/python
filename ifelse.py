number = int(input("Enter the number :"))

if(number>=0):
    print("Number is greater then zero")
    if(number%2==0):
        print("Number is even")
    else:
        print("Number is odd")
elif(number==0):
    print("Number is zero itself")    
else:
    print("Number is less than zero")
    if(number/2==0):
        print("Number is even")
    else:
        print("Number is odd")

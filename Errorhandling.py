def error(a):
    num = int(input("Enter a number: "))
    ans = a/num
    print(ans)

list1 = [1,2,3]

try:
    # for i in list1:
    #     print(list1[i+1])
    error(8)
except ArithmeticError:
    print("Error related to Arithmatic")
except ValueError:
    print("Value entered is wrong") 
except Exception as e:
    print("Any Error happened")    


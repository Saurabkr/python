if __name__ == "__main__":
 def fabonacci(a):
    if(a==0):
        return 0
    elif(a==1):
        return 1
    else:
        return fabonacci(a-1) + fabonacci(a-2)


for i in range(7):
    print(fabonacci(i))


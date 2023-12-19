import time

def timeWhileLoop():
    i = 0 
    while(i<50000):
        print(i)
        i += 1

def timeForLoop():
    for i in range(50000):
        print(i)

# init = time.time()
# print(timeWhileLoop())
# t1 = time.time() - init

# init = time.time()
# print(timeForLoop())
# print(time.time() - init)
# print(t1)


print("hi there!")
time.sleep(10)
print("I am wake up again")

t = time.strftime("%H:%M:%S")
print(t)

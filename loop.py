#print the number till 2000
# for number in range(2001):
for number in range(1,101):
    print(number)

for number in range(1,101,2): # print number with difference of 2
    print(number, end=',')   

#while loop, else with while

x=0

while(x<5):
    print(x)
    x+=1

x = 5
while(x>0):
    print(x)
    x-=1    
else:
    print("while loop stopped")

#emulate do-while loop in phython

i=0
while True:
    print(i)
    i+=1
    if(i==1):
        print("Number is zero")
        break




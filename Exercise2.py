import time

# tm = str(time.strftime('%H:%M:%S'))
tm = '22:55:00'

if(tm>='00:00:00' and tm<='12:00:00'):
    print("Good Morning")
elif(tm>'12:00:00' and tm<='16:00:00'):
    print("Good Afternoon")
else:
    print("Good Evening")

# we can also convert input to integer then apply if-else    


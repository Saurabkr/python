list1 = [27,85,93,829,76,89]

for i in list1:    
    if(i%2==0):
        print("We get the even number",i)
        break
    print(i)

for i in list1:    
    if(i%2==0):
        print("Skipped",i)
        continue
    print(i)
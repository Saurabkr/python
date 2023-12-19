listDemo = [1,29,74,37,28]

index = 0
for i in listDemo:
    
    if index == 2:
        print(f"{i} is saurab's number")
    else:
        print(i)  
    index += 1      

# same code using enumerate

for i,value in enumerate(listDemo):
    
    if i==2:
        print(f"{value} is saurab's number")
    else:
        print(value)    
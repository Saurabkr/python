# import random
# listTemp = [2,3,4,5,9,50,22,76]

# print(random.choice(listTemp))
# dictionary = {"First prime minister of INDIA":'Pt. Jawahar Lal Nehru', }

listQuestion = ["First prime minister of INDIA?", "What is 5-3/3?"]
listAns =["Pt. Ji","4"]
sum=0
for i in listQuestion,listAns:
    print(i)
    # sumT += sum
    ans = input("Enter your ans: ")
    if(ans==i):
        sum+=100
        break
    else:
        print("You Loose!")
        break    
print(sum)

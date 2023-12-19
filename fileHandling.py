#to create a file
f = open("myFile.txt",'a')

#To read the file
letter = open("myFile.txt",'r')
print(letter.read())


#To write in that file
letter = open("myFile.txt",'w')
letter.write("Hi buddy i am python! ")
letter.close()

letter = open("myFile.txt",'a')
letter.write("see my magic. ")
letter.close()

# we can use this to append/write without using f.close()
with open("myFile.txt",'a') as f:
    f.write("hi everybody")



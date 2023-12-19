# with open("table.txt",'w') as f:
#     f.write("1234567890saurab")

# with open("table.txt",'r') as f:
#     f.seek(10)
#     print(f.tell())
#     print(f.read(6))

with open("table.txt",'w') as f:
    f.write("hi there")
    f.truncate(2)

with open("table.txt",'r') as f:     
 print(f.read()) 

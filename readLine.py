#Readline function read line by line

f = open('file.txt','r')

i=0
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f'B{i} Marks of math : {m1}')
    print(f'B{i} Marks of Soience : {m2}')
    print(f'B{i} Marks of SST : {m3}')

    print(line)





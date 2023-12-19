l = [2,3,5,7,9,8,26,37,13,73,94,22,7,23]
print(l[:4])
print(l[-2:4])
print(l[0::2])

# for i in l:
#     print(i)

#creating list on fly
l1 = [i*i for i in range(5)]
print(l1)
print(l1[::2])

#ex1
l2=["saurab","kanak","timro"]
names = [name for name in l2 if 'r' in name]
print(names)

#ex2
l3=[23,9,749,383,45678,2736,765]
print([number for number in l3 if number%2==0])

#try not to use like this 
l4 = l3
l4[0] = 45
print(l4,l3) # it will change the l3 as well as l4 list

#list functions

list1 = [2,6,4,2,7,8,6,9]

print(list1.count(2))
list1.append(76)
print(list1.index(2))
#copy list
cpy = list1.copy()
print(cpy)
#concatenate
combineList = cpy+l3
print(combineList)

list1.insert(2,5)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)


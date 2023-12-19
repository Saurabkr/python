tup = (2,3,4,"saurab")

print(tup[2])

tup2 = (1)
print(type(tup2)) #In this case type is integer for this you have to add ,

tup3 = (1,)
print(type(tup3))

#tuple is immutable so if we want to change the tuple then convert it into list

list1 = list(tup)
list1.append("changed")
list1.insert(2,9)
tup = tuple(list1)
print(tup)

#concatenate
tup1 = (5,9,0,8)

tupTemp = tup + tup1
print(tupTemp)

#tuple functions
temp = tup.index(9,2,8)
print(temp)

temp1 = tup.count(9)
print(temp1)
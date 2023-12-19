setEx = {}
print(type(setEx)) #dict

setEx1 = set()
print(type(setEx1)) #set

setM = {2,4,"vickey","zeta",9,2} #No Duplicates, No replace
print(setM)

for i in setM:
    print(i)

#Function of set

set1 = {1,2,3,4,5,6}
set2 = {3,56,2,8,9}

set3 = set1.union(set2)
print(set3)
print(set1.union(set2))
print(set1, set2)

print(set1.intersection(set2))
set1.intersection_update(set2)
print(set1)
print(set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print(set1)

set3 = {1,2,3,4,5,6}
set4 = {3,56,2,8,9}
print(set3.difference(set4))
print(set3.isdisjoint(set4))
print(set3.isdisjoint(set4))





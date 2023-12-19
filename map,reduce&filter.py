from functools import reduce

list1 = [1,4,2,6,9,3]

ans = reduce(lambda x,y: x+y , list1)

print(ans)

#Map

res = list(map(lambda x: x*x, list1))
print(res)

#Filter

result = list(filter(lambda x: (x>5), list1))
print(result)
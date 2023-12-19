dict1 = {101:"surab",102:"shibam",103:"shoeb", 104:"aktar"}

print(dict1.keys())
print(dict1.values)

#way to take the key value pair
for i in dict1.keys():
    print(f'This is key = {i} and this is value {dict1[i]}')

for key,value in dict1.items():
    print(f'This is key = {key} and this is value {value}')    

#Method or function of dictionry

dict1.update({105:'shubham',106:'thakur'})    
print(dict1)

dict1.pop(102)
print(dict1)

dict1.popitem()
print(dict1)

dict2 = dict1.copy()
print(dict2)


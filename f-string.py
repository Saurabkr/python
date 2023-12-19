#String formatting using string function
str = "my name is {} and i am a {}"
name ='saurab'
position = 'SDET'
print(str.format(name,position))

str1 = "i have a {1} and it's name is {0}"
AnimalType = 'Dog'
DogName = 'Tiger'
print(str1.format(DogName,AnimalType))

#f-string : String formatting
print(f'my name is {name} and i am a {position}')

size = 34
print(f'My T-shirt size is {size:.3f}')

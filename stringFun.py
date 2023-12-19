str = '''i am a good boy
who like to travel'''

for character in str:
   print(character)

#string slicing :   

name = "Harry"

print(name[-4:-2]) # name[len(name)-4:len(name)-2]
print(name[:]) #by default python will take name[0:len(name)]
print(name[1:4])#first index is included whereas second is exclude eg. 1 included and 4 is excluded
print(name[:-3])
print(name[-1:-4]) #name[5-1:5-4] = name[4:1] -> no meaning that's why result not printed

exmp = "saurab is a goOd orator and have leadership quality too"

print(exmp.capitalize())
print(exmp.endswith("too"))
print(exmp.startswith("saurab"))
print(exmp.split())
print(exmp.find("a"))
print(exmp.index("is"))
print(exmp.title())
print(exmp.replace("a","the"))
print(exmp.center(100))
print(exmp.isalpha())
print(exmp.isalnum())
print(exmp.rstrip("o"))
print(exmp.upper())
print(exmp.lower())
print(exmp.swapcase())

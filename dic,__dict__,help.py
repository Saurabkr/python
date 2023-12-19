#dir() -> use to get info about the object
x = [1,2,3,4]
print(dir(x))

class example:
    def __init__(self, name, id):
        self.name = name
        self.id = id



a = example("saurab",102)
print(a.__dict__)

print(help(example))




class Student:
    def __init__(self, name, rollNo):
        self.__name = name
        self.__rollNo = rollNo

    def intr(self):
        print(f"My name is {self.__name} and Roll No. is {self.__rollNo}")

class Saurab(Student):
    def stream(self):
        print("Science")        

student1 = Student("subhas",'102')
student1.intr()

#inheritance
a = Saurab("saurab",'102')
a.intr()
a.stream()

#private in python define by __value(and access outside class by _class name__attribute) and protected in _value
# access using Name Mangling
print(student1._Student__name)
print(student1._Student__rollNo)            
class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    # def emp(self):
    #     print(f"{self.name} earns {int(self.salary)}")
    @classmethod
    def strInput(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

# e = employee("harry", "1500")
# e.emp()

string = "saurab-120000"
e1 = Employee.strInput(string)
print(e1.name, e1.salary)


       



class DataScience:
    def __init__(self,topic,language):
        self.topic = topic
        self.language = language

    def toLearn(self):
        print(f"To learn Data Science you need to know {self.topic} and {self.language}")

    def __str__(self):
        return "This class provide guide to ace DS "   

    def __repr__(self):
        return "In this we learn DS basic"

    def __call__(self, *args, **kwds):
        for i in args:
            print(i)

        for i in kwds:
            print(kwds.get(i))   


s = DataScience("Statitics","python")

print(s)
s(["ml","DL", "PowerBI"], {1:'integration', 2:'Linear Regrassion', 3:'Probablity'})            

             

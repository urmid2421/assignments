class Student:

    def setName(self,name):
        self.name = name
    def getName(self):
        print(self.name)
    def setRollNumber(self,roll_number):
        self.roll_number = roll_number 
    def getRollNumber(self):
        print(self.roll_number)
    

obj = Student()
obj.setName("Urmi")
obj.setRollNumber(24)
obj.getName()
obj.getRollNumber()
class student :
    def __init__(self,name,rollno):
        self.name=name
        self.rollno = rollno

    def show(self):
        print(self.name,self.rollno)
    class laptop :
        def __init__(self):
            self.brand = "hp"
            self.cpu = "i8"
            self.ram = 16
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 =student("navin",2)
s2 = student("jenny",3)
s1.show()
lap1 = student.laptop()
print(lap1.brand)
lap1.show()

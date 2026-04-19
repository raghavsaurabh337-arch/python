#method  are funtion that belongs to a object
class Student:
    college_name="IIMT college"
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def wel(self):
        print("welcome to")
        
    def display(self):
        print("my name is ",self.name)
        print("my age is ",self.age)


    def get_marks(self):
        print(self.marks)
        return self.marks


s1=Student("raghav",19,98)
s1.wel()
# s1.get_marks()
s1.display()
print(s1.get_marks())
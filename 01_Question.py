# create student  class that takes & marks  of 3 subject as argument in cosntructor. then create a method to print tha average.\
class Student:
     def __init__(self , name ,marks):
          self.name=name
          self.marks=marks
     def average(self):
      avg=sum(self.marks)/len(self.marks)
      print("average marks of ",self.name,"is ",avg)

s1=Student("Raghav",[89,90,91])
s1.average()
s1.name="Raghav Kumar"
s1.average()
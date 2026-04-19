class Student:
    college_name="IIMT COllege"  #class attribute # class variable or atibute created inside the class but outside the constructor  
    #parameterized constructor
    def __init__(self,name,age):
    #   print(self)
      self.name=name #object attribyute
      self.ge=age
      print("This is a constructor")
      print("my name is ",self.name)  

s1=Student("raghav",19)   
print(s1.college_name,s1.name,s1.ge)
s2=Student("priya",20)
print(s2.name,s2.ge)
print(Student.college_name) # class variable can be accessed by class name also without creating object of the class

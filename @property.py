class Student:
     def __init__(self,math,hindi,phy):
          self.math=math
          self.hindi=hindi
          self.phy=phy
          self.pa=str(round((self.math+self.hindi+self.phy)/3,2))+"%"
     @property
     def pade(self):
          return str((self.math+self.hindi+self.phy)/3)+"%"




s1=Student(98,90,89)   
print(s1.pa)    
s1.math=100
print(s1.pade)   
print(s1.math)
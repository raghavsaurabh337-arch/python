class pattern:
     def simple(self):
          for i in range(5):
               print("*",end="")
     def simple2(self):
          for i in range(5):
               print("*")
     def simple3(self):
          for i in range(5):
               print("*"*i)
     def simple4(self):
          for i in range(5,0,-1):
               print()
               print("*"*i)
     def simple5(self):
          for i in range(0,100):
               print(i)          
               
          
   
obj=pattern()
obj.simple()
obj.simple2()
obj.simple3()
obj.simple4()
obj.simple5()





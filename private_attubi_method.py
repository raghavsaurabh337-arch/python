class Account:
     def __init__(self,Acc_no,password):
          self.Acc_no=Acc_no
          self.__password=password  # this is private attribute


     def show(self):
         print(self.__password) 


ac=Account(1381000,"Raghav@321")
print(ac.Acc_no)
#print(ac.password)    
print(ac.show())      
          
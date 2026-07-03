for i in range(1,20):
     print(i)

class pattren  :
     def five(self):
          for i in range(1,6):
               print("*")
     def five_by_five(self):
          for i in range(1,6):
               for j in range(1,6):
                    print("*", end=" ")
               print()
obj=pattren()
obj.five()
obj.five_by_five()

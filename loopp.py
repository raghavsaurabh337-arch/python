for i in range(1,20):
     print(i)

class pattren  :
     def star(self):
          for i in range(1,6):
               print("*")
     def squareStar(self):
          for i in range(1,6):
               for j in range(1,6):
                    print("*", end=" ")
               print()

     def half(self):
          for i in range(1,6):
             
                print("*"* i )
obj=pattren()
# obj.star()
# obj.squareStar()
obj.half()

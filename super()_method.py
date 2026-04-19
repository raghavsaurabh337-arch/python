# import super_method
class car:
     def __init__(self,color):
          self.color=color
     @staticmethod
     def start():
          print("Car started")
     @staticmethod     
     def stop():
          print("car is stopped")

class toytaCar(car):
     def __init__(self,name,color):
          super().start()
          self.name=name
          super().__init__(color)
         

car1=toytaCar("Swite","Black")
print(car1.name)
print(car1.color)




          
class car:
     color="black"
     @staticmethod
     def start():
          print("Car started")
     @staticmethod     
     def stop():
          print("car is stopped")

class toytaCar(car):
     def __init__(self,name):
          self.name=name


car1=toytaCar("fortuner")
car2=toytaCar("prius")
print(car1.name)
print(car1.stop())

          
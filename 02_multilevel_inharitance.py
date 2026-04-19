class car:
     color="black"
     def start():
          print("Car started")    
     def stop():
          print("car is stopped")

class toytaCar(car):
     def __init__(self,name):
          self.name=name

class forfuner(toytaCar):
     def _init__(self,type,name):
          self.type=type
          super.__init__(name)


car1=forfuner("swite","BMW")
#print(car1.type)
print(car1.start())



          
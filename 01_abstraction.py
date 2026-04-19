# cheejo ko chhupana abstraction kehlata hai
# abstraction me hum sirf important cheejo ko dikhate hai aur baki chhupate hai
# abstraction ke 2 tarike hote hai
# 1. method abstraction  
# 2. data abstraction
class car:
     def __init__(self):
          self.acc= False
          self.clutch= False
          self.gear= 0
     def start(self):
          self.acc= True
          self.clutch= True
          self.gear= 1
          print("car started...")
car1=car()
car1.start()
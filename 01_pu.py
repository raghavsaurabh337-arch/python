# class MyClass:
#     variable = "blah"

#     def function(self):
#         print("This is a message inside the class.")
# obj=MyClass()
# obj2=MyClass()
# # obj.function()
# obj.variable="saurabh"
# print(obj.variable)
# print(obj2.variable)



# class NumberHolder:

#    def __init__(self, number): # ye funcation kuch bhi retun nhi krta ha iski value kahi use krni ha to self.number se user kr lo
#        self.number = number
       
#    def returnNumber(self):
#        print(self.number)

#    def num(self):
#        print(self.number)    

# var = NumberHolder(7)
# var.returnNumber()
# var.num(34)
# # print(var.returnNumber())



# define the Vehicle class
# class Vehicle:
#     name = ""
#     kind = "car"
#     color = ""
#     value = 100.00
    
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         return desc_str
# # your code goes here
# car1=Vehicle()
# car1.name = "Fer"
# car1.color = "red"
# car1.kind = "convertible"
# car1.value = 60000.00

# car2=Vehicle()
# car2.name = "Jump"
# car2.color = "blue"
# car2.kind = "van"
# car2.value = 10000.00
# # test code
# print(car1.description())
# print(car2.description())


# Create a class
class Person:
        def __init__(self,name,age):
              self.name=name
              self.age=age


        def greet(self):
            print("Hello, my name ",self.name)
            print("Age",self.age)

p1=Person("john",36)
p1.greet()



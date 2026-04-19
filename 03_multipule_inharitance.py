class base1:
     def fun1(self):
          print("this is base1 ")
class base2():
     def base2_fun3(self):
          print("this is base2")
class derived(base1, base2):
     def derive_fun3(self):
          print("this is derived class ")

c1=derived()
print(c1.fun1())                    
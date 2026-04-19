class student:
     def __init__(self,name):
          self.name=name


S = student("sachin")
print(S.name)
del S.name
print(S.name)          
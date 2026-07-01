def student(**kwargs):
    print(kwargs)

student(name="Saurabh", age=22)

def arr(*args):
    for arg in args:
        print(arg)
        
arr(1, 2, 3)
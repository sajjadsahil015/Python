class myMetaClass(type):
    def __new__(cls,name,bases,dct):
        print(f"{name} class is under development!")
        return super().__new__(cls,name,bases,dct)
class MyClass(metaclass=myMetaClass):
    pass

class AutoStrMthd(type):
    def __new__(cls,name,bases,dct):
        if "__str__" not in dct:
            dct["__str__"]= lambda self: f"{name} class"
        return super().__new__(cls,name,bases,dct)

class String(metaclass=AutoStrMthd):
    pass

c = String()
print(c)


class RequireIniMthd(type):
    def __new__(cls,name,bases,dct):
        if '__init__' not in dct:
            raise TypeError("Init method is missing!")
        return super().__init__(cls,name,bases,dct)

class Person(metaclass=RequireIniMthd):
    def __init__(self,name):
        self.name= name

# class Animal(metaclass=RequireIniMthd):
#     pass

class UpperAttrMthd(type):
    def __new__(cls,name,bases,dct):
        new_dct = {}
        for key,value in dct.items():
            if not key.startswith("__"):
                new_dct[key.upper()] = value
            else:
                new_dct[key] = value
        return super().__new__(cls, name, bases, new_dct)

class Dog(metaclass=UpperAttrMthd):
    breed = "Husky"
    color = "White"

print(hasattr(Dog, 'breed')) 
print(hasattr(Dog, 'BREED')) 

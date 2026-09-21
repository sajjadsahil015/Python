def add_greetings(cls):
    def greet(self):
        return f"Hello {self.__class__.__name__}: {self.name}"
    cls.greet = greet
    return cls

@add_greetings
class Person:
    def __init__(self,name):
        self.name = name

person = Person(4,3)
print(person.greet())

class Decorator:
    def __init__(self,function):
        self.function = function

    def __call__(self,a,b):
        result = self.function(a,b)
        return result**2
    
@Decorator
def add(a,b):
    return a+b

print(add(2,3))


class CountCalls:
    def __init__(self,func):
        self.func = func
        self.count_calls = 0
    def __call__(self, *args, **kwargs):
        self.count_calls+=1
        print(f"{self.func.__name__}#{self.count_calls} times called")
        return self.func(*args,*kwargs)
@CountCalls
def function(name):
    print(f"Hello {name}")

function("ALi")
function("Alice")
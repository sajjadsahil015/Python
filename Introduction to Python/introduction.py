#Example of bytecode 

class Person: # Class Person (source code/blue print of an object at runtime)
    def __init__(self, name: str, age: int): # initilizer or constructor which is responsible to create Object in memory at runtime
        self.name = name           # Pereson attibute
        self.age = age             # Pereson attibute

    def greet(self): # Person Class method greet()
        print(f"Hello, my name is {self.name} and I am {self.age} years old.") # Print/Output to console/terminal

# Lets create a Person object in memory
person: Person = Person("Sajjad Hassan", 20)

person.greet() 
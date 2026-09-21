class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name  
        self.age = age    

   
    def display(self):
        print(f"{self.name} is {self.age} years old and is a {self.species}.")

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

print(f"Dog species: {Dog.species}")
print(f"Buddy's species: {dog1.species}")  
print(f"Max's species: {dog2.species}")

print(f"Buddy's name: {dog1.name}") 
print(f"Max's age: {dog2.age}") 
Dog.species = "Canis lupus"
print(f"Buddy's species after modification: {dog1.species}")
print(f"Max's species after modification: {dog2.species}")
dog1.species = "Canis aureus"
print(f"Buddy's species after shadowing: {dog1.species}")
print(f"Max's species remains: {dog2.species}") 

print(f"Dog class attributes: {Dog.__dict__}")
print(f"dog1 instance attributes: {dog1.__dict__}")
print(f"dog2 instance attributes: {dog2.__dict__}")
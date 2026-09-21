from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> None:
        pass

class Dog(Animal):
    def speak(self) -> None:
        print(type(self), ":  Woof!")

class Cat(Animal):
    def speak(self) -> None:
        print(type(self), ":  Meow!")

def animal_sound(animal: Animal) -> None:
    animal.speak()

dog = Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)
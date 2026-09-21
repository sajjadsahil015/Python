class Car:
    def __init__(self, color, speed):
        self.color = color  # Public attribute
        self.__speed = speed  # Private attribute (encapsulated)

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed
car = Car("red", 0) 
print("Current speed: ", car.get_speed()) 

for i in range(5):
    car.accelerate()

print("Speed after acceleration: ", car.get_speed())
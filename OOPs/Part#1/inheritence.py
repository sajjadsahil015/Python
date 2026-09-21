class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        print("Driving Speed = ", self.speed)

    def accelerate(self):
        self.speed += 10


class Car(Vehicle):
    def __init__(self, color, speed):
        super().__init__(color, speed)


class Truck(Vehicle):
    def __init__(self, color, speed):
        super().__init__(color, speed)

car = Car("red", 120)
truck = Truck("blue", 80)

car.drive()
truck.drive()
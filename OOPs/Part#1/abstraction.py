from rich import print
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._engine_status = False
        self._idling_time = 0
        self._traffic_signal = None

    def drive(self):
        if self._engine_status and self._traffic_signal == "green":
            print(f"You are driving a {self.brand} {self.model}.")
        elif self._traffic_signal == "red":
            print(f"You stopped at the red light in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        else:
            self._start_engine()
            print(f"You are driving a {self.brand} {self.model}.")

    def stop(self):
        if self._engine_status:
            print(f"You stopped the {self.brand} {self.model}.")
            self._idle_stop_engine()
        else:
            print(f"The {self.brand} {self.model} is already stopped.")

    def set_traffic_signal(self, signal):
        self._traffic_signal = signal
        if signal == "red":
            print(f"Traffic signal turned red. You stopped in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        elif signal == "green":
            print(f"Traffic signal turned green. You can drive your {self.brand} {self.model}.")
            if not self._engine_status:
                self._start_engine()

    def _start_engine(self):
        self._engine_status = True
        self._idling_time = 0
        print("Engine started.")
    def _idle_stop_engine(self):
        import time
        print("Engine is idling...")
        for i in range(5):
            print(f"Idling time: {i+1} seconds")
            time.sleep(1)
            self._idling_time += 1
        if self._idling_time >= 5:
            self._engine_status = False
            print("Engine stopped (idle stop) to save fule.")

my_car = Car("Toyota", "Camry")
my_car.set_traffic_signal("green")
my_car.drive()
my_car.set_traffic_signal("red")
# my_car.set_traffic_signal("green")
# my_car.drive()


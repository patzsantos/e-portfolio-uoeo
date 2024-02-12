class DriverlessCar:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def info(self):
        print(f"This model of this driverless car is {self.model}, made in{self.year}.")


class CarControl:
    def __init__(self):
        pass

    def steer(self):
        print("Steer")

    def accelerate(self):
        print("Accelerate")

    def brake(self):
        print("Brake")

driverless_car = DriverlessCar("Toyota", 2014)
car_control = CarControl()

for car in (driverless_car, car_control):
    car.info()
    car_control.steer()
    car_control.accelerate()
    car_control.brake()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.data = {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "traffic_light": {
                "red": "stop",
                "yellow": "slow",
                "green": "go"
            },
            "car_control": ["steer left", "steer right", "steer straight", "accelerate", "brake"],
            "avoid_object": ["human", "animal", "big rock", "another car"]
        }

    def items(self):
        return self.data.items()

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()


my_car = Car("Mazda", "CX 5", 2019)

print("Items:")
print(my_car.items())

print("\nKeys:")
print(my_car.keys())

print("\nValues:")
print(my_car.values())

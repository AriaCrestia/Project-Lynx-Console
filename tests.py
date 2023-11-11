class Car:
    def __init__(self, colour, mileage):
        self.colour = str(colour)
        self.mileage = int(mileage)
    def __str__(self):
        return f"The {self.colour} has {self.mileage:,} miles."

car1 = Car("blue", 20000)
car2 = Car("red", 30000)

for car in (car1, car2):
    print(car)
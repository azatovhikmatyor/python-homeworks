class Car:
    def __init__(self, yearModel, make):
        self.yearModel = yearModel
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def get_speed(self):
        return self.speed


# Demonstration of the Car class
car = Car(2022, "Toyota")

# Accelerating
print("Accelerating:")
for _ in range(5):
    car.accelerate()
    print(f"Current speed: {car.get_speed()} mph")

# Braking
print("\nBraking:")
for _ in range(5):
    car.brake()
    print(f"Current speed: {car.get_speed()} mph")

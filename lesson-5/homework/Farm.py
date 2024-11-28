# Parent class Animal
class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Child class Cow
class Cow(Animal):
    def __init__(self, name, age, weight, milk_production):
        super().__init__(name, age, weight)
        self.milk_production = milk_production  # liters per day

    def moo(self):
        print(f"{self.name} the cow says 'Moo!'")

    def produce_milk(self):
        print(f"{self.name} produces {self.milk_production} liters of milk per day.")


# Child class Chicken
class Chicken(Animal):
    def __init__(self, name, age, weight, egg_count):
        super().__init__(name, age, weight)
        self.egg_count = egg_count  # eggs per week

    def cluck(self):
        print(f"{self.name} the chicken says 'Cluck!'")

    def lay_eggs(self):
        print(f"{self.name} lays {self.egg_count} eggs per week.")


# Child class Pig
class Dog(Animal):
    def __init__(self, name, age, weight, bark):
        super().__init__(name, age, weight)
        self.bark = bark

    def oink(self):
        print(f"{self.name} says 'Wof wof!'")

    def roll_in_mud(self):
        print(f"{self.name} is rolling in their favorite mud spot: {self.favorite_mud_spot}.")


# Demonstration of the farm animals with methods
print("Farm Animals:")

cow = Cow("Bessie", 5, 700, 20)
cow.eat()
cow.moo()
cow.produce_milk()

chicken = Chicken("Clucky", 2, 1.5, 7)
chicken.eat()
chicken.cluck()
chicken.lay_eggs()

pig = Dog("Doggy", 3, 200, "near the barn")
pig.eat()
pig.oink()
pig.bark()

from animal import Animal


class Bird(Animal):
    def __init__(self, name, age, isSuperPredator, calPerMeal, flightHeight, wingsLength):
        Animal.__init__(self, name, age, isSuperPredator, calPerMeal)
        self.flightHeight = flightHeight
        self.wingsLength = wingsLength

    def __str__(self):
        return Animal.__str__(self) + "This is a bird. Its wings are " + str(
            self.wingsLength) + "cm long and flies " + str(self.flightHeight) + "m\n"

    def eat(self):
        return super().eat() - 10

    def sing(self):
        print("la la lo la")

    def dance(self):
        print("Back-flip")
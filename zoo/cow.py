from mammal import Mammal


class Cow(Mammal):
    def __init__(self, name, age, isSuperPredator, calPerMeal, calInMilk, numPreMonths, numBirths):
        Mammal.__init__(self, name, age, isSuperPredator, calPerMeal, calInMilk, numPreMonths)
        self.numBirths = numBirths

    def __str__(self):
        return Mammal.__str__(self) + "This is a cow. It had " + str(self.numBirths) + " births.\n"

    def eat(self):
        return super().eat()/4

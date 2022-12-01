from mammal import Mammal


class Hipo(Mammal):
    def __init__(self, name, age, isSuperPredator, calPerMeal, calInMilk, numPreMonths, fatPercent):
        Mammal.__init__(self, name, age, isSuperPredator, calPerMeal, calInMilk, numPreMonths)
        self.fatPercent = fatPercent

    def __str__(self):
        return Mammal.__str__(self) + "This is a hipo. It has " + str(self.fatPercent) + "% fat.\n"

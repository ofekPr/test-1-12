from animal import Animal


class Mammal(Animal):
    def __init__(self, name, age, isSuperPredator, calPerMeal, calInMilk, numPreMonths):
        Animal.__init__(self, name, age, isSuperPredator, calPerMeal)
        self.calInMilk = calInMilk
        self.numPreMonths = numPreMonths

    def __str__(self):
        return Animal.__str__(self) + "This is a mammal. It has " + str(
            self.calInMilk) + " calories in milk and pregnant for " + str(
            self.numPreMonths) + " months.\n"

    def eat(self):
        return super().eat() + self.calInMilk

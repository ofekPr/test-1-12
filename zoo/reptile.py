from animal import Animal


class Reptile(Animal):
    def __init__(self, name, age, isSuperPredator, calPerMeal, tailLength):
        Animal.__init__(self, name, age, isSuperPredator, calPerMeal)
        self.tailLength = tailLength

    def __str__(self):
        return Animal.__str__(self) + "This is a reptile. Its tail is " + str(self.tailLength) + "cm long\n"
from reptile import Reptile


class Crocodile(Reptile):
    def __init__(self, name, age, isSuperPredator, calPerMeal, tailLength, hadTeethTreat):
        Reptile.__init__(self, name, age, isSuperPredator, calPerMeal, tailLength)
        self.hadTeethTreat = hadTeethTreat

    def __str__(self):
        return Reptile.__str__(self) + "This is a crocodile. Had teeth treatment? " + str(self.hadTeethTreat) + "\n"

    def eat(self):
        return super().eat() * 10

from reptile import Reptile


class Snake(Reptile):
    def __init__(self, name, age, isSuperPredator, calPerMeal, tailLength, isPoisonous):
        Reptile.__init__(self, name, age, isSuperPredator, calPerMeal, tailLength)
        self.isPoisonous = isPoisonous

    def __str__(self):
        return Reptile.__str__(self) + "This is a snake. Is poisonous? " + str(self.isPoisonous) + "\n"

    def dance(self):
        print("##Cool_Dance_Moves##")

from cow import Cow


class Bull(Cow):
    def __init__(self, name, age, isSuperPredator, calPerMeal, calInMilk, numPreMonths, numBirths, hornLength):
        Cow.__init__(self, name, age, isSuperPredator, calPerMeal, calInMilk, numPreMonths, numBirths)
        self.hornLength = hornLength

    def __str__(self):
        return Cow.__str__(self) + "This is a bull. It's horn is " + str(self.hornLength) + " cm.\n"

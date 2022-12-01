from bird import Bird


class Pigeon(Bird):
    def __init__(self, name, age, isSuperPredator, calPerMeal, flightHeight, wingsLength, color):
        Bird.__init__(self, name, age, isSuperPredator, calPerMeal, flightHeight, wingsLength)
        self.color = color

    def __str__(self):
        return Bird.__str__(self) + "This is a pigeon. It's color is: " + self.color + "\n"
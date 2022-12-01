from reptile import Reptile
from bird import Bird


class Park:
    def __init__(self):
        self.animals = [None] * 1000
        self.count = 0

    def add(self, animal):
        if self.count < 1000:
            self.animals[self.count] = animal
            self.count += 1

    def oldSuperPred(self):
        oldSuperPredList = []
        for animal in self.animals:
            if animal and animal.age > 10 and animal.isSuperPredator:
                oldSuperPredList.append(animal)
        return oldSuperPredList

    def numSuperPreditor(self):
        num = 0
        for animal in self.animals:
            if animal and type(animal) == Reptile or type(animal) == Bird and animal.isSuperPredator:
                num += 1
        return num

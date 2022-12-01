from animal import Animal
from mammal import Mammal
from reptile import Reptile
from bird import Bird
from cow import Cow
from hipo import Hipo
from crocodile import Crocodile
from snake import Snake
from pigeon import Pigeon
from bull import Bull
from park import Park


def calPerDay(animals):
    summ = 0
    for animal in animals:
        summ += animal.eat()
    return summ


def birdSinging(animals):
    for animal in animals:
        if issubclass(type(animal), Bird):
            animal.sing()


def dancing(animals):
    for animal in animals:
        if issubclass(type(animal), Bird) or issubclass(type(animal), Snake):
            animal.dance()


def fattestHipo(animals):
    fatHipo = None
    for animal in animals:
        if issubclass(type(animal), Hipo):
            if fatHipo is None or animal.fatPercent > fatHipo.fatPercent:
                fatHipo = animal
    return fatHipo.name


animal1 = Animal("a", 16, True, 150)
print(animal1)

mammal1 = Mammal("b", 16, False, 150, 150, 12)
print(mammal1)

reptile1 = Reptile("c", 17, False, 300, 12)
print(reptile1)

bird1 = Bird("d", 15, True, 300, 100, 40)
print(bird1)

cow1 = Cow("e", 20, False, 100, 200, 6, 10)
print(cow1)

hipo1 = Hipo("f", 10, False, 10, 20, 5, 8)
print(hipo1)

crocodile1 = Crocodile("g", 20, False, 300, 80, False)
print(crocodile1)

snake1 = Snake("h", 18, True, 300, 40, True)
print(snake1)

pigeon1 = Pigeon("i", 3, False, 20, 20, 40, "gray")
print(pigeon1)

bull1 = Bull("j", 19, False, 200, 400, 12, 20, 40)
print(bull1)

print(animal1.eat())

print(mammal1.eat())

print(cow1.eat())

print(bird1.eat())

print(crocodile1.eat())

bird1.sing()

bird1.dance()
snake1.dance()

print(calPerDay([animal1, mammal1, cow1, bird1, crocodile1, snake1]))

birdSinging([animal1, mammal1, cow1, bird1, crocodile1, pigeon1, snake1])

dancing([animal1, mammal1, cow1, bird1, crocodile1, pigeon1, snake1])

print(fattestHipo([animal1, mammal1, cow1, bird1, hipo1, crocodile1, pigeon1, snake1]))

park1 = Park()

park1.add(animal1)
park1.add(mammal1)
park1.add(cow1)
park1.add(bird1)
park1.add(hipo1)
park1.add(crocodile1)

print(park1.oldSuperPred(), park1.numSuperPreditor())

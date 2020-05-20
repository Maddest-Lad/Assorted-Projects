import math
import random as rnd


# Create 2d array of numbers to serve as coordinates for entities
def createCoordinatePlane(inputpopulation):
    temp = []
    output = []
    for _ in range(int(math.sqrt(inputpopulation))):
        temp.append("H  ")
    for _ in range(int(math.sqrt(inputpopulation))):
        output.append(temp.copy())
    return output


# Prints out the entire map of all the entities so it is easy to understand what is happening
def printEntityMap(inputmap):
    for r in inputmap:
        for c in r:
            print(c, end="")
        print()


# Outputs whether the 2d array contains a certain value
def contains(array, userinput):
    count = 0
    for row in array:
        for each in row:
            if each == userinput:
                count += 1
    return True if count > 0 else False


# Called repeatedly until every person is recovered from the illness or dead
def tickWorld(array, infectionrate, recoveryrate, fatalityrate):
    infected = []
    eligible_infections = []
    # Add every infected person to the list 'infected'
    for row in range(len(array)):
        for column in range(len(array)):
            if array[row][column] == "I  ":
                infected.append([row, column])
    # Get coordinates of every person around the infected person
    for each_infected in infected:
        temp = [[each_infected[0] - 1, each_infected[1] - 1], [each_infected[0] - 1, each_infected[1]],
                [each_infected[0] - 1, each_infected[1] + 1], [each_infected[0], each_infected[1] + 1],
                [each_infected[0] + 1, each_infected[1] + 1], [each_infected[0] + 1, each_infected[1]],
                [each_infected[0] + 1, each_infected[1] - 1], [each_infected[0], each_infected[1] - 1]]
        eligible_infections.extend(temp.copy())
    # Remove coordinates of entities that are not really in the grid
    for coordinate in eligible_infections.copy():
        if coordinate[0] == -1 or coordinate[1] == -1 or coordinate[0] == len(array) or coordinate[1] == len(array):
            eligible_infections.remove(coordinate)
    for entity in eligible_infections:
        if array[entity[0]][entity[1]] == "H  ":
            infection_seed = rnd.randint(0, 100)
            if infection_seed <= infectionrate * 100:
                array[entity[0]][entity[1]] = "I  "
    for entity in infected:
        recovery_seed = rnd.randint(1, 100)
        fatality_seed = rnd.randint(1, 100)
        if recovery_seed <= recoveryrate * 100:
            array[entity[0]][entity[1]] = "R  "
        elif fatality_seed <= fatalityrate * 100:
            array[entity[0]][entity[1]] = "D  "
    return array
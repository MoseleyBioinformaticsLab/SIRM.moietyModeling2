#!/usr/bin/python3

"""
SAGA4.py is used to find the optimal solution.
"""
# This file is modified to put the results of SAGA optimization into file using logging.
import random
import math
import jsonpickle



class ElementDescription:
    """ Description of element in a SAGA Guess."""

    def __init__(self, low=0, high=0, name='', value=None, mutate=None):
        """
        :param low: minimum value for this element; OPTIONAL if immutable value specified.
        :param high: maximum value for this element; OPTIONAL if immutable value specified.
        :param name: OPTIONAL - the name of the element.
        :param value: OPTIONAL - immutable value for this element.
        :param mutate: the method that calculates a mutation; DEFAULT - ElementDescription.mutatePopulationRangedFloat.
        """
        self.low = low
        self.high = high
        self.name = name
        self.value = value
        self.immutable = True if value is not None else False
        self.mutate = self.mutatePopulationRangedFloat if mutate is None else mutate

    def mutateRandomRangedFloat(self):
        """
        :return: random floating point value between an element's range.
        """
        return random.random() * (self.high - self.low) + self.low

    def mutateRandomRangedInteger(self):
        """
        :return: random integer value between an element's range.
        """
        return int(0.5 + random.random() * (self.high - self.low) + self.low)

    def mutatePopulationRangedFloat(self, range, fraction):
        """
        :param range: the range of the element value among population.
        :param fraction: number change along the temperature, as the temperature decreases the fraction decreases.
        :return: random floating point between shrinking ranges based on the values in the population, current temp, and the alpha.
        """
        high = self.high
        low = self.low
        if fraction < 1:
            low = self.low * fraction + range[0] * (1 - fraction)
            high = self.high * fraction + range[1] * (1 - fraction)
        return random.random() * (high - low) + low

    def mutatePopulationRangedInteger(self, range, fraction):
        """
        :param range: the range of the element value among population.
        :param fraction: number change along the temperature, as the temperature decreases the fraction decreases.
        :return: random integer value between shrinking ranges based on the values in the population, current temp, and the alpha.
        """
        high = self.high
        low = self.low
        if fraction < 1:
            low = self.low * fraction + range[0] * (1 - fraction)
            high = self.high * fraction + range[1] * (1 - fraction)
        return int(0.5 + random.random() * (high - low) + low)


class Guess:
    """ The basic unit of the solution. """

    def __init__(self, elementDescriptions, elements, energy=0):
        """
        :param elementDescriptions: a list of ElementDescription objects.
        :param elements: a list of the value for the corresponding elementDescription.
        :param energy: the energy of this Guess.
        """
        self.elementDescriptions = elementDescriptions
        self.elements = elements
        self.energy = energy

    def clone(self):
        """Clones everything but the energy.

        :return: the Guess object.
        """
        return Guess(self.elementDescriptions, self.elements)

    def __str__(self):
        """Converts Guess to a string representation.

        :return: the string representation.
        """
        string = "Guess: Energy = {0} Parameters: ".format(self.energy)
        for index in range(0, len(self.elementDescriptions)):
            if self.elementDescriptions[index].name != '':
                string += str(self.elementDescriptions[index].name)
            else:
                string += "Element {0}".format(index+1)
            string += " = {0} ".format(self.elements[index])
        return string


class GuessAdapter:
    """
    To convert optimization solution to Guess format.
    """

    def __init__(self, elements, energy):
        """
        :param elements: a list of value to parameters.
        :param energy: the energy of this solution.
        """
        self.elements = elements
        self.energy = energy


class Population:
    """ A certain number of Guess objects compose the Population. """

    def __init__(self, bestIndex=-1, maxEnergy=0, lowestEnergy=0):
        """
        :param bestIndex: the index of the Guess with maximum energy(direction:1) or minimum energy(direction:-1)
        :param maxEnergy: the range of the energy among the population.
        :param lowestEnergy: the minimum energy when direction is 1 and the maximum energy when direction is -1.
        """
        self.guesses = []
        self.edRangeTuples = []
        self.ranges = []
        self.elementDescriptions = []
        self.bestIndex = bestIndex
        self.maxEnergy = maxEnergy
        self.lowestEnergy = lowestEnergy
        self._bestGuess = None

    def initialize(self, size, elementDescriptions, energyCalculation, direction, initialPopulation=None):
        """
        :param size: the number of Guess objects in the population.
        :param elementDescriptions: a list of ElementDescription objects of the Guess
        :param energyCalculation: the function used to calculate the energy.
        :param direction: (1 or -1) for determining lowest energy.
        :param initialPopulation: an initial Population object.
        :return: the initialized Population object.
        """
        self.elementDescriptions = elementDescriptions
        self.ranges = [[0, 0] for eDescrip in self.elementDescriptions]
        self.edRangeTuples = [ (eDescrip, range) for (eDescrip, range) in zip(self.elementDescriptions, self.ranges)]

        if initialPopulation:
            self.ranges = initialPopulation.ranges
            self.edRangeTuples = initialPopulation.edRangeTuples
            if initialPopulation.bestIndex >= 0:
                size -= 1
                self.guesses.append(initialPopulation.guesses[initialPopulation.bestIndex].clone())

        for iteration in range(0, size):
            newElements = [eDescrip.value if eDescrip.immutable else eDescrip.mutate(eRange, 1) for (eDescrip, eRange) in self.edRangeTuples]
            self.guesses.append(Guess(self.elementDescriptions, newElements))

        for guess in self.guesses:
            guess.energy = energyCalculation(guess.elements)

        energies = [guess.energy for guess in self.guesses]
        if direction > 0 :
            self.bestIndex = max(range(len(energies)), key=energies.__getitem__)
        else:
            self.bestIndex = min(range(len(energies)), key=energies.__getitem__)

        for elementIndex in range(0, len(self.guesses[0].elements)):
            self.updateRange(elementIndex)
        self.updateLowestEnergy(direction)
        self.updateMaxEnergy()

        return self

    def updateGuess(self, newGuess, index, direction):
        """Updates guess in the population and RETURNS the old Guess.

        :param newGuess: a new Guess object.
        :param index: the index of the Guess that will be replaced by the newGuess.
        :param direction: 1 or -1.
        :return: the old Guess.
        """
        oldGuess = self.guesses[index]
        oldElements = oldGuess.elements
        self.guesses[index] = newGuess

        if direction * newGuess.energy <= direction * self.lowestEnergy:
            self.lowestEnergy = newGuess.energy

        for elementIndex in range(0, len(newGuess.elements)):
            if newGuess.elements[elementIndex] <= self.ranges[elementIndex][0]:
                self.ranges[elementIndex][0] = newGuess.elements[elementIndex]
            elif newGuess.elements[elementIndex] >= self.ranges[elementIndex][1]:
                self.ranges[elementIndex][1] = newGuess.elements[elementIndex]
            elif oldElements[elementIndex] == self.ranges[elementIndex][0] or oldElements[elementIndex] == self.ranges[elementIndex][1]:
                self.updateRange(elementIndex)

        # Update maxEnergy
        self.updateMaxEnergy()

        return oldGuess

    def updateLowestEnergy(self, direction):
        """Updates the lowestEnergy in the population.

        :param direction: 1 or -1.
        :return: no return.
        """
        energies = [guess.energy for guess in self.guesses]
        energies.sort()
        self.lowestEnergy = energies[0] if direction > 0 else energies[-1]

    def updateMaxEnergy(self):
        """Updates maxEnergy in the Population.

        :return: no return.
        """
        maxEnergy = self.guesses[self.bestIndex].energy
        alternativeMaxEnergy = abs(maxEnergy - self.lowestEnergy)
        maxEnergy = abs(maxEnergy)
        self.maxEnergy = alternativeMaxEnergy if alternativeMaxEnergy > maxEnergy else maxEnergy

    def updateRange(self, elementIndex):
        """Updates ranges for each element in the Population.

        :return: no return.
        """
        rangeValue = [ guess.elements[elementIndex] for guess in self.guesses ]
        rangeValue.sort()
        self.ranges[elementIndex][0:2] = (rangeValue[0], rangeValue[-1])

    @property
    def bestGuess(self):
        return self.guesses[self.bestIndex]


class SAGA:
    """ Implements a stimulated annealing / genetic algorithm optimization strategy. """

    def __init__(self, stepNumber, startTemperature, temperatureStepSize, alpha, populationSize, energyCalculation, direction=-1,
                 elementDescriptions=None, startPopulation=None, initialPopulation=None, crossoverRate=0.1, crossover=None, acceptedCriteria=None,
                 mutationRate=1, annealMutationRate=1, maxEnergy=None, crossoverProbabilities=None, validGuess=None, bestOperation=None,
                 bestResultsFile=None, allResultsFile=None):
        """
        :param stepNumber: number of simple steps to perform.
        :param startTemperature: starting temperature.
        :param temperatureStepSize: number of simple steps in a temperature step.
        :param alpha: power of annealing rate; 1 is linear.
        :param populationSize: size of the population of Guesses.
        :param energyCalculation: function to calculate the energy.
        :param direction: optimization direction; 1 is maximizing; -1 is minimizing; DEFAULT is -1.
        :param elementDescriptions: OPTIONAL - list of ElementDescription objects.
        :param startPopulation: OPTIONAL - Population object to use as the starting population.
        :param initialPopulation: OPTIONAL - Population object to initialize with.
        :param crossoverRate: fractional rate of crossover versus mutation; DEFAULT is 0.1.
        :param mutationRate: number of mutations to perform in creating a new Guess; DEFAULT is 1.
        :param annealMutationRate: whether to anneal mutationRate with temperature; DEFAULT is 1.
        :param maxEnergy: OPTIONAL - override of maxEnergy for SA calculation.
        :param validGuess: function that tests if a Guess object is valid. DEFAULT is None.
        :param bestOperation: function to perform on best Guess object; DEFAULT is None.
        """
        self.elementDescriptions = [] if elementDescriptions is None else elementDescriptions
        self.stepNumber = stepNumber
        self.startTemperature = startTemperature
        self.temperatureStepSize = temperatureStepSize
        self.energyCalculation = energyCalculation
        self.alpha = alpha
        self.direction = direction
        self.startPopulation = startPopulation
        self.initialPopulation = initialPopulation
        self.mutationRate = mutationRate
        self.annealMutationRate = annealMutationRate
        self.crossoverRate = crossoverRate
        self.crossover = self.createCrossoverGuess if crossover is None else crossover
        self.acceptedCriteria = self.boltzamannAcceptedCriteria if acceptedCriteria is None else acceptedCriteria
        self.validGuess = validGuess
        self.populationSize = populationSize
        self.maxEnergy = maxEnergy
        self.bestOperation = bestOperation
        self.crossoverProbabilities = [i/sum(crossoverProbabilities) for i in crossoverProbabilities] if crossoverProbabilities is not None else None
        self.bestResultsFile = bestResultsFile if bestResultsFile else None
        self.allResultsFile = allResultsFile if allResultsFile else None

    def addElementDescriptions(self, *elementDescriptions):
        """Add elementDescriptions.

        :param elementDescriptions: the elementDescription objects.
        """
        self.elementDescriptions.extend(elementDescriptions)

    def optimize(self):
        """Performs the optimization.

        :return: the Population object.
        """
        if self.startPopulation:
            self.populationSize = len(self.startPopulation.guesses)
            population = self.startPopulation
        else:
            population = Population()
            population.initialize(self.populationSize, self.elementDescriptions, self.energyCalculation, self.direction, self.initialPopulation)

        maxEnergy = self.maxEnergy if self.maxEnergy else population.maxEnergy
        numberOfTemperatureSteps = int(self.stepNumber / self.temperatureStepSize)
        temperature = self.startTemperature
        temperatureFraction = 1
        temperatureStepCount = 0

        stepCount = self.stepNumber
        while stepCount:
            """Update temperature."""
            if not stepCount % self.temperatureStepSize:
                temperatureStepCount += 1
                temperature = self.startTemperature * pow((1.0 - temperatureStepCount/numberOfTemperatureSteps), self.alpha)
                temperatureFraction = (temperature + 0.01) / (self.startTemperature + 0.01)
                if self.annealMutationRate:
                    self.mutationRate = int(self.mutationRate * temperature / self.startTemperature)
                    if not self.mutationRate:
                        self.mutationRate = 1
                if self.allResultsFile:
                    for index in range(0, len(population.guesses)):
                        self.allResultsFile.write(jsonpickle.encode(population.guesses[index]))

            """Create new guess and test it."""
            testIndex = random.randrange(len(population.guesses))
            oldGuess = population.guesses[population.bestIndex].clone()
            newGuess = self.crossover(population, testIndex, oldGuess) if self.crossoverRate > random.random() else self.createMutationGuess(population, testIndex, oldGuess, self.mutationRate, temperatureFraction)
            newGuess.energy = self.energyCalculation(newGuess.elements)

            if self.direction * newGuess.energy > self.direction * population.guesses[population.bestIndex].energy:
                population.bestIndex = testIndex

            if self.acceptedCriteria(population, testIndex, newGuess, temperature, maxEnergy):
                oldGuess = population.updateGuess(newGuess, testIndex, self.direction)
                maxEnergy = self.maxEnergy if self.maxEnergy else population.maxEnergy
                if testIndex == population.bestIndex:
                    if self.bestResultsFile:
                        self.bestResultsFile.write(jsonpickle.encode(newGuess))
                    self.bestOperation and self.bestOperation(newGuess)
                elif self.allResultsFile:
                    self.allResultsFile.write(jsonpickle.encode(newGuess))
            elif self.allResultsFile:
                self.allResultsFile.write(jsonpickle.encode(newGuess))
            stepCount -= 1

        if self.allResultsFile:
            for index in range(0, len(population.guesses)):
                self.allResultsFile.write(jsonpickle.encode(population.guesses[index]))
        return population

    def decentAcceptedCriteria(self, population, testIndex, newGuess, temperature=None, maxEnergy=None):
        """Decent criteria used for the acceptance of the new guess"""

        return self.direction * population.guesses[testIndex].energy <= self.direction * newGuess.energy

    def boltzamannAcceptedCriteria(self, population, testIndex, newGuess, temperature=None, maxEnergy=None):
        """Boltzamann criteria used for the acceptance of the new guess"""

        return self.direction * (self.direction * temperature * maxEnergy * math.log(random.random()) * (testIndex != population.bestIndex) +
                             population.guesses[testIndex].energy) <= self.direction * newGuess.energy

    def createMutationGuess(self, population, targetIndex, newGuess, mutationRate, temperatureFraction):
        """Creates and RETURNS a new mutated Guess.

        :param population: the Population object.
        :param targetIndex: index of Guess in the Population used to create a new Guess.
        :param newGuess: a Guess object that will be recreated.
        :param mutationRate: number of mutations to perform in creating a new Guess; DEFAULT is 1.
        :param temperatureFraction: number change along the temperature, as the temperature decreases the fraction decreases.
        :param validGuess: function that tests if a Guess object is valid. DEFAULT is 0.
        :return: the new Guess.
        """
        newGuess.elements = list(population.guesses[targetIndex].elements)
        while True:
            count = mutationRate
            while count:
                elementIndex = random.randrange(len(newGuess.elements))
                if not newGuess.elementDescriptions[elementIndex].immutable:
                    count -= 1
                    newGuess.elements[elementIndex] = newGuess.elementDescriptions[elementIndex].mutate(population.ranges[elementIndex], temperatureFraction)
            if not self.validGuess or self.validGuess(newGuess):
                break
        return newGuess

    def createCrossoverGuess(self, population, targetIndex, newGuess):
        """Creates and RETURNS a new Guess via a crossover between two Guesses.

        :param population: the Population object.
        :param targetIndex: index of Guess in the Population used to create a new Guess.
        :param newGuess: a Guess object that will be recreated.
        :return: the new Guess.
        """
        while True:
            newGuess.elements = list(population.guesses[targetIndex].elements)
            cross = self.getCrossoverTarget(population, targetIndex)
            crossElements = population.guesses[cross].elements
            start = random.randint(0, len(crossElements) - 1)
            finish = random.randint(start+1, len(crossElements))
            newGuess.elements[start:finish+1] = crossElements[start:finish+1]
            if not self.validGuess or self.validGuess(newGuess):
                break
        return newGuess

    def createRandomCrossoverGuess(self, population, targetIndex, newGuess):
        """Creates and RETURNS a new Guess via a random crossover between two Guesses.

        :param population: the Population object.
        :param targetIndex: index of Guess in the Population used to create a new Guess.
        :param newGuess: a Guess object that will be recreated.
        :return: the new Guess.
        """
        while True:
            newGuess.elements = list(population.guesses[targetIndex].elements)
            cross = self.getCrossoverTarget(population, targetIndex)
            crossElements = population.guesses[cross].elements
            numberOfChange = random.randint(1, len(crossElements))
            pickedPoints = []
            while numberOfChange:
                crossPoint = random.randrange(len(newGuess.elements))
                if crossPoint not in pickedPoints:
                    newGuess.elements[crossPoint] = crossElements[crossPoint]
                    pickedPoints.append(crossPoint)
                    numberOfChange -= 1
            if not self.validGuess or self.validGuess(newGuess):
                break
        return newGuess

    def createPotentialPointCrossoverGuess(self, population, targetIndex, newGuess):
        """Creates and RETURNS a new Guess via the potential point crossover between two Guesses.

        :param population: the Population object.
        :param targetIndex: index of Guess in the Population used to create a new Guess.
        :param newGuess: a Guess object that will be recreated.
        :return: the new Guess.
        """
        if self.crossoverProbabilities is None:
            self.crossoverProbabilities = [1 / len(self.elementDescriptions) for i in self.elementDescriptions]
        while True:
            newGuess.elements = list(population.guesses[targetIndex].elements)
            cross = self.getCrossoverTarget(population, targetIndex)
            crossElements = population.guesses[cross].elements
            start = random.random()
            finish = start + random.random() * (1 - start)
            countProbability = 0
            startPoint = 0
            for startPoint in range(len(self.crossoverProbabilities)):
                countProbability += self.crossoverProbabilities[startPoint]
                if countProbability > start:
                    break
            finishPoint = startPoint
            for finishPoint in range(startPoint+1, len(self.crossoverProbabilities)):
                countProbability += self.crossoverProbabilities[finishPoint]
                if countProbability > finish:
                    break
            newGuess.elements[startPoint : finishPoint+1] = crossElements[startPoint : finishPoint+1]
            if not self.validGuess or self.validGuess(newGuess):
                break
        return newGuess

    def getCrossoverTarget(self, population, excludedTarget):
        """Finds a new crossoverTarget weighted towards individuals with high energy.

        :param population: the Population object.
        :param excludedTarget: index of Guess in the Population that is excluded as a crossoverTarget.
        :return: the index of the Guess used as crossTarget.
        """

        lowestEnergy = population.lowestEnergy
        totalEnergy = sum([abs(guess.energy - lowestEnergy) for guess in population.guesses])

        crossTarget = excludedTarget
        while crossTarget == excludedTarget:
            findEnergy = random.random() * totalEnergy
            countEnergy = 0
            for crossTarget in range(len(population.guesses)):
                countEnergy += abs(population.guesses[crossTarget].energy - lowestEnergy)
                if countEnergy >= findEnergy:
                    break
            if crossTarget > len(population.guesses) - 1:
                crossTarget = random.randrange(len(population.guesses))
        return crossTarget







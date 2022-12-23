"""
    Advent of Code 2022, Day 1:

Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on
Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The
Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th.
Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along
the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition
traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One
important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that
they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory
(if any) by a blank line.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many
Calories are being carried by the Elf carrying the most Calories. Find the Elf carrying the most Calories.

"""


def getElf (calorieArray):
    """ Iterates through array, returning
        the maximum value """

    maxCals = 0

    for element in calorieArray:
        if element > maxCals:
            maxCals = element
    return maxCals


def generateCalorieArray(fileName):
    """ Generates an array of calories held by
        each elf in the given file. """

    # Initialize a file object
    file = open(fileName, "r")

    # Read the file into an array, splitting by lines
    fileArr = file.read().split("\n")

    # Initialize a variable for storing the current elf's calorie count and an array for storing the counts
    currentElf = 0
    calorieArray = []

    # Iterate through the lines of the array
    for element in fileArr:
        # Add up the calories for each elf
        if element != '':
            currentElf += int(element)
        # Add the final calorie count into the array to return
        else:
            calorieArray.append(currentElf)
            currentElf = 0

    return calorieArray


if __name__ == '__main__':
    arr = generateCalorieArray("calories.txt")
    print("The elf carrying the most calories hass ", getElf(arr), " calories")



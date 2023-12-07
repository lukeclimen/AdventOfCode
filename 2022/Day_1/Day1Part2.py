"""
    Advent of Code 2022, Day 1, Part 2:

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most
Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three
Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000
Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""


def getElf(calorieArray):
    """Iterates through array, returning
    the 3 maximum values"""

    mostCals = 0
    secondMost = 0
    thirdMost = 0

    # Iterate through the calorie array
    for element in calorieArray:
        # Replacing the top elf
        if element > mostCals:
            thirdMost = secondMost
            secondMost = mostCals
            mostCals = element

        # Replacing the second from top elf
        elif element > secondMost:
            thirdMost = secondMost
            secondMost = element

        # Replacing the third from top elf
        elif element > thirdMost:
            thirdMost = element

    return mostCals + secondMost + thirdMost


def generateCalorieArray(fileName):
    """Generates an array of calories held by
    each elf in the given file."""

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
        if element != "":
            currentElf += int(element)
        # Add the final calorie count into the array to return
        else:
            calorieArray.append(currentElf)
            currentElf = 0

    return calorieArray


if __name__ == "__main__":
    arr = generateCalorieArray("calories.txt")
    print(
        "The elfs carrying the top 3 most calories have ",
        getElf(arr),
        " total calories",
    )

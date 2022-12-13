"""
    Advent of Code 2022, Day 4, Part 2:

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of
pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9,
2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

"""

import re

def readAssignments(fileName):
    """ This function returns an array of numbers, with each group of 4 representing one pair of elves' tasks.
        The array contains char values, as we can cast them to ints as we use them in the future. I couldn't
        figure out how to cast them to ints in a way that didn't require another traversal of the array. """
    file = open(fileName, 'r')
    fileArray = []

    for index, line in enumerate(file):
        splitLine = re.findall(r'\d+', line)
        fileArray += splitLine

    return fileArray


def anyOverlap(elf1Low, elf1High, elf2Low, elf2High):
    """ This function reads in the low and high bounds for two elves' assignments and determines whether
        either elf's assignments has any overlap with the other's. """

    # See if there are any "sandwiches" of a high-low pair around another end point. Ex:
    #
    # elf1igh
    # ...       elf2High
    # elf1Low
    #

    # elf1 sandwiching either end of elf2
    if (elf1Low <= elf2High and elf1High >= elf2High) or (
        elf1Low <= elf2Low and elf1High >= elf2Low
    ):
        return True

    # elf2 sandwiching either end of elf1
    if (elf2Low <= elf1High and elf2High >= elf1High) or (
            elf2Low <= elf1Low and elf2High >= elf1Low
    ):
        return True

    return False

if __name__ == '__main__':
    # Read in the file
    elfArray = readAssignments("assignments.txt")
    # Initialize variable to store total overlap pairs
    overlapSum = 0
    for index in range(0, len(elfArray), 4):
        # Casting the values to integers here
        if anyOverlap(int(elfArray[index]), int(elfArray[index + 1]), int(elfArray[index + 2]), int(elfArray[index + 3])):
            overlapSum += 1

    # Show the number of pairs that have any overlap
    print(overlapSum)

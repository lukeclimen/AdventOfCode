"""
    Advent of Code 2022, Day 3, Part 2:

As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For
efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if
a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most
two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges
need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item
type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item
type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg

And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges.
In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for
the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those
item types?

"""


def readFile(fileName):
    """ This function returns an array filled with the contents of a given file,
        with each element representing a line from the file. """
    file = open(fileName, 'r')
    return file.read().split("\n")


def findCommonItem(elf1, elf2, elf3):
    """ This function returns the duplicate letter (case sensitive) in a given string. """
    # Inserting to a dictionary, stopping on duplicate value
    letterDict = {}

    # Add all letters from elf1 to the dictionary
    for letter in elf1:
        letterDict[letter] = 1

    # Set repeated letters in elf2 to have the value '2' in the dictionary
    # Not incrementing, because of possible repeated items in the rucksack
    for letter in elf2:
        if letter in letterDict:
            letterDict[letter] = 2

    # Once we find the letter that is repeated in elf3 (value of 2 in the dictionary)
    # We know that we have found the "badge" value
    for letter in elf3:
        if letter in letterDict:
            if letterDict[letter] == 2:
                return letter


def getPriority(elf1, elf2, elf3):
    """ This function returns an integer based on the priority value specified in the instructions. The function
        calls the findCommonItem function to get the needed letter"""

    # Find the common letter and convert it to ASCII number code
    letter = findCommonItem(elf1, elf2, elf3)
    asciiValue = ord(letter)

    # If the value is capital, subtract 38 to map it to the priority value
    if asciiValue < 95:
        return asciiValue - 38
    # Otherwise, subtract 96 to map it to the priority value
    else:
        return asciiValue - 96


if __name__ == '__main__':
    # Getting the rucksack array contents and initializing a summing variable
    ruckArray = readFile("rucksack.txt")
    prioritySum = 0

    # Iterate through the rucksacks in steps of 3 and get their content priorities
    for index in range(0, len(ruckArray), 3):
        prioritySum += getPriority(ruckArray[index], ruckArray[index + 1], ruckArray[index + 2])

    print(prioritySum)

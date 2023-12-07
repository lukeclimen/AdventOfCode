"""
    Advent of Code 2022, Day 3:

One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that
Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two
compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help
finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to
different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same
number of items in each of its two compartments, so the first half of the characters represent items in the first
compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

     - The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the
    items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears
    in both compartments is lowercase p.
     - The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears
    in both compartments is uppercase L.
     - The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
     - The fourth rucksack's compartments only share item type v.
     - The fifth rucksack's compartments only share item type t.
     - The sixth rucksack's compartments only share item type s.

To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p),
38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item
types?

"""


def readFile(fileName):
    """This function returns an array filled with the contents of a given file,
    with each element representing a line from the file."""
    file = open(fileName, "r")
    return file.read().split("\n")


def findCommonItem(itemString):
    """This function returns the duplicate letter (case sensitive) in a given string."""
    # Inserting to a dictionary, stopping on duplicate value
    letterDict = {}

    # Insert the letters from compartment 1 into the dictionary
    for index in range(0, len(itemString) // 2):
        letterDict[itemString[index]] = True

    # Check if the letters in compartment 2 already exist in the dictionary
    for index in range(len(itemString) // 2, len(itemString)):
        if itemString[index] in letterDict:
            return itemString[index]


def getPriority(itemString):
    """This function returns an integer based on the priority value specified in the instructions. The function
    calls the findCommonItem function to get the needed letter"""

    # Find the common letter and convert it to ASCII number code
    letter = findCommonItem(itemString)
    asciiValue = ord(letter)

    # If the value is capital, subtract 38 to map it to the priority value
    if asciiValue < 95:
        return asciiValue - 38
    # Otherwise, subtract 96 to map it to the priority value
    else:
        return asciiValue - 96


if __name__ == "__main__":
    # Getting the rucksack array contents and initializing a summing variable
    ruckArray = readFile("rucksack.txt")
    prioritySum = 0

    # Iterate through the rucksacks and get their content priorities
    for ruckSack in ruckArray:
        prioritySum += getPriority(ruckSack)

    print(prioritySum)

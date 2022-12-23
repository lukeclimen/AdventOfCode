"""
    Advent of Code 2022, Day 5, Part 2:

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover
9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup
holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the
same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be
ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each
stack?

"""
import re


def readMoves(fileName):
    """ This function reads in the numbers (3 per line) and outputs them into a list, which is returned. """
    file = open(fileName, 'r')
    fileList = []

    for index, line in enumerate(file):
        fileList += re.findall(r'\d+', line)

    return fileList


def readCrates(fileName):
    """ This function reads in lines from a CSV file representing a stack of crates. It returns a list of
        strings. """
    csvFile = open(fileName, 'r')
    fileList = []
    crateArray = []
    crateString = ""

    for index, line in enumerate(csvFile):
        # Read in a list of characters
        crateArray = re.findall(r'[A-Za-z]+', line)
        # Convert the list to a string
        for letter in crateArray:
            crateString += letter
        #Store the string
        fileList.append(crateString)
        crateString = ""

    return fileList


def simulateRearrangement(moveList, crateList):
    """ This function simulates the different steps laid out in moveList on the
        items found in crateList. It returns a string of the top characters in each
        stack of crates after all moves have been executed. """

    # Iterate through the move list, in steps of 3 (crates to move, stack moving from, stack moving to)
    for index in range(0, len(moveList), 3):
        cratesToMove = int(moveList[index])
        stackFrom = int(moveList[index + 1])
        stackTo = int(moveList[index + 2])
        # Simulate this move on the crateList
        simulateMove(cratesToMove, stackFrom, stackTo, crateList)

    # Once all moves are done, pop the top crate off of each stack and form a string
    crateString = ""
    for index in range(0, len(crateList)):
        crateString += crateList[index][-1:]

    return crateString


def simulateMove(cratesToMove, stackFrom, stackTo, crateList):
    """ This function simulates the crate rearrangements made from one 'move' from the CSV file,
        comprising of a number of crates to move, from which stack and to which stack. This function
        does not return a value, but does change crateList. """
    # Using slices instead of pop/append to retain order
    movedCrate = crateList[stackFrom - 1][-cratesToMove:]
    crateList[stackTo - 1] += movedCrate
    # Then delete the slice from the crate stack that it was moved from
    crateList[stackFrom - 1] = crateList[stackFrom - 1][:-cratesToMove]


if __name__ == '__main__':
    moveList = readMoves("moves.txt")
    crateList = readCrates("crates.csv")
    topCrates = simulateRearrangement(moveList, crateList)
    print(topCrates)
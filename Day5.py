"""
    Advent of Code 2022, Day 5:

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks
of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or
fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which
crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input).
For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N
is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a
single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack
to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack
1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate
to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up
below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in
stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

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
        stacks. """
    csvFile = open(fileName, 'r')
    fileList = []

    for index, line in enumerate(csvFile):
        fileList.append(re.findall(r'[A-Za-z]+', line))

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
        crateString += crateList[index].pop()

    return crateString


def simulateMove(cratesToMove, stackFrom, stackTo, crateList):
    """ This function simulates the crate rearrangements made from one 'move' from the CSV file,
        comprising of a number of crates to move, from which stack and to which stack. This function
        does not return a value, but does change crateList. """
    for iteration in range(0, cratesToMove):
        movedCrate = crateList[stackFrom - 1].pop()
        crateList[stackTo - 1].append(movedCrate)

if __name__ == '__main__':
    moveList = readMoves("moves.txt")
    crateList = readCrates("crates.csv")
    topCrates = simulateRearrangement(moveList, crateList)
    print(topCrates)
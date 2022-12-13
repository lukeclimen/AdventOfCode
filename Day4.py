"""
    Advent of Code 2022, Day 3:

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been
assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a
range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the
assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big
list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

For the first few pairs, this list means:

    Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second
    Elf was assigned sections 6-8 (sections 6, 7, 8).
    The Elves in the second pair were each assigned two sections.
    The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also
    got 7, plus 8 and 9.

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger
numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

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


def totalOverlap(elf1Low, elf1High, elf2Low, elf2High):
    """ This function reads in the low and high bounds for two elves' assignments and determines whether
        either elf's assignments completely encapsulates the other's. """

    # If elf1's low bound is lower or equal to elf2's, check if elf1's high bound is also higher
    # or equal to elf2's. This would indicate elf1's assignments totally overlap elf2's
    if elf1Low <= elf2Low and elf1High >= elf2High:
        return True

    # Otherwise, see if elf2's high bound is higher than elf1's. This would mean that elf2's
    # assignments totally overlap elf1's
    elif elf2Low <= elf1Low and elf2High >= elf1High:
        return True

    return False


if __name__ == '__main__':
    # Read in the file
    elfArray = readAssignments("assignments.txt")
    # Initialize variable to store total overlap pairs
    totalOverlapSum = 0
    for index in range(0, len(elfArray), 4):
        # Casting the values to integers here
        if totalOverlap(int(elfArray[index]), int(elfArray[index + 1]), int(elfArray[index + 2]), int(elfArray[index + 3])):
            totalOverlapSum += 1

    # Show the number of pairs that have total overlap
    print(totalOverlapSum)

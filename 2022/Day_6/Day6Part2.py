"""
    Advent of Code, Day 6, Part 2:

Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs
to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather
than 4.

Here are the first positions of start-of-message markers for all of the above examples:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first start-of-message marker is detected?
"""
import Day_6.Day6


def findMarker(signalString):
    """
    This function reads a string and returns the index is the position of the 14th consecutive unique character.
    :param signalString: string
    :return: markerIndex
    """
    markerIndex = 4
    # Iterate through the signal string
    for index in range(len(signalString)):
        if index < 4:
            continue
        # Use the 32 bits of an integer to check for repeated characters
        charBit = 0
        isMarker = True
        for i in range(14):
            bitIndex = ord(signalString[index - i]) - ord("a")
            if (charBit & (1 << bitIndex)) > 0:
                isMarker = False
                break
            else:
                charBit = charBit | (1 << bitIndex)

        if isMarker:
            return index

    return -1


if __name__ == "__main__":
    signal = Day_6.Day6.readSignal("signal.txt")
    print(findMarker(signal) + 1)

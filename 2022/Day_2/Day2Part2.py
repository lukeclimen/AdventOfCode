"""
    Advent of Code 2022, Day 2, Part 2:

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs
to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round
ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also
    choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of
    1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
according to your strategy guide?

"""


def roundOutcome(opponent, winLoseDraw):
    """Determines what hand gesture (R/P/S) I choose based on my opponent"""
    # Evaluate needing to throw a rock
    if (
        (opponent == "A" and winLoseDraw == "Y")
        or (opponent == "B" and winLoseDraw == "X")
        or (opponent == "C" and winLoseDraw == "Z")
    ):
        return 1

    # Evaluate needing to throw a paper
    elif (
        (opponent == "A" and winLoseDraw == "Z")
        or (opponent == "B" and winLoseDraw == "Y")
        or (opponent == "C" and winLoseDraw == "X")
    ):
        return 2

    # Otherwise, I need to throw scissors
    return 3


def round(opponent, winLoseDraw):
    """Determines the score of a round of R/P/S"""

    # Set the score based on if I need to Win, Lose or Draw
    if winLoseDraw == "X":
        resultScore = 0
    elif winLoseDraw == "Y":
        resultScore = 3
    else:
        resultScore = 6

    # Return the round score plus the score of the Win/Loss/Draw
    return resultScore + roundOutcome(opponent, winLoseDraw)


def simulateStrategy(fileName):
    """Generates a score based on the given strategy guide."""

    # Initialize a file object and a variable to store my score
    file = open(fileName, "r")
    myScore = 0

    # Read the file into an array, splitting by lines
    fileArr = file.read().split("\n")

    # Iterate through the array, simulating the game rounds
    for element in fileArr:
        theirChoice, winLoseDraw = element.split(" ")

        # Evaluate the outcome of the round
        myScore += round(theirChoice, winLoseDraw)

    return myScore


if __name__ == "__main__":
    score = simulateStrategy("stratguide.txt")
    print("The score obtained by following the strategy guide is ", score, " points")

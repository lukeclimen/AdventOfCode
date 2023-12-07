"""
    Advent of Code 2022, Day 2:

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock
Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each
simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected:
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round
instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say
will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C
for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for
each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for
Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if
you were to follow the strategy guide.

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you
    with a score of 8 (2 because you chose Paper + 6 because you won).

    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for
    you with a score of 1 (1 + 0).

    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

"""


def roundOutcome(opponent, myself):
    """Determines the outcome of R/P/S based on my selection and my opponent's"""
    # Evaluate a win
    if (
        (myself == "X" and opponent == "C")
        or (myself == "Y" and opponent == "A")
        or (myself == "Z" and opponent == "B")
    ):
        return 6

    # Evaluate a draw
    elif (
        (myself == "X" and opponent == "A")
        or (myself == "Y" and opponent == "B")
        or (myself == "Z" and opponent == "C")
    ):
        return 3

    # Otherwise, it was a loss
    return 0


def round(opponent, myself):
    """Determines the score of a round of R/P/S"""
    # Set the initial score based on my selection for R/P/S
    if myself == "X":
        initialScore = 1
    elif myself == "Y":
        initialScore = 2
    else:
        initialScore = 3

    # Return the initial score plus the score of the Win/Loss/Draw
    return initialScore + roundOutcome(opponent, myself)


def simulateStrategy(fileName):
    """Generates a score based on the given strategy guide."""

    # Initialize a file object and a variable to store my score
    file = open(fileName, "r")
    myScore = 0

    # Read the file into an array, splitting by lines
    fileArr = file.read().split("\n")

    # Iterate through the array, simulating the game rounds
    for element in fileArr:
        theirChoice, myChoice = element.split(" ")

        # Evaluate the outcome of the round
        myScore += round(theirChoice, myChoice)

    return myScore


if __name__ == "__main__":
    score = simulateStrategy("stratguide.txt")
    print("The score obtained by following the strategy guide is ", score, " points")

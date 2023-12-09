# --- Part Two ---
# Just as you're about to report your findings to the Elf, one of you realizes that
# the rules have actually been printed on the back of every card this whole time.

# There's no such thing as "points". Instead, scratchcards only cause you to win more
# scratchcards equal to the number of winning numbers you have.

# Specifically, you win copies of the scratchcards below the winning card equal to the
# number of matches. So, if card 10 were to have 5 matching numbers, you would win one
# copy each of cards 11, 12, 13, 14, and 15.

# Copies of scratchcards are scored like normal scratchcards and have the same card
# number as the card they copied. So, if you win a copy of card 10 and it has 5
# matching numbers, it would then win a copy of the same cards that the original card
# 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies
# cause you to win any more cards. (Cards will never make you copy a card past the end
# of the table.)

# This time, the above example goes differently:

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# Card 1 has four matching numbers, so you win one copy each of the next four cards:
# cards 2, 3, 4, and 5.
# Your original card 2 has two matching numbers, so you win one copy each of cards 3
# and 4.
# Your copy of card 2 also wins one copy each of cards 3 and 4.
# Your four instances of card 3 (one original and three copies) have two matching
# numbers, so you win four copies each of cards 4 and 5.
# Your eight instances of card 4 (one original and seven copies) have one matching
# number, so you win eight copies of card 5.
# Your fourteen instances of card 5 (one original and thirteen copies) have no
# matching numbers and win no more cards.
# Your one instance of card 6 (one original) has no matching numbers and wins no more
# cards.
# Once all of the originals and copies have been processed, you end up with 1 instance
# of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of card 4, 14
# instances of card 5, and 1 instance of card 6. In total, this example pile of
# scratchcards causes you to ultimately have 30 scratchcards!

# Process all of the original and copied scratchcards until no more scratchcards are
# won. Including the original set of scratchcards, how many total scratchcards do you
# end up with?

from part_one import convert_file_into_array, _split_numbers


def _determine_card_score(winning_numbers_string: str, numbers_had_string: str) -> int:
    """Scores each card against rules of the game and returns score"""
    card_total = 0
    winning_number_list = winning_numbers_string.split()
    numbers_had_list = numbers_had_string.split()
    for number in winning_number_list:
        if number in numbers_had_list:
            card_total += 1
    return card_total


def _increment_next_n_card_totals(
    starting_card_index: int,
    card_list: list[int],
    next_n_cards: int,
    increment_value: int,
) -> list[int]:
    """Increments the next n cards by the given increment, starting at the given index"""
    for n in range(next_n_cards):
        card_list[starting_card_index + n] += increment_value
    return card_list


def _sum_total_cards_in_pile(total_amount_of_each_card: list[int]) -> int:
    """Counts up the total for each card in the card pile"""
    sum = 0
    for card in total_amount_of_each_card:
        sum += card
    return sum


if __name__ == "__main__":
    card_list = convert_file_into_array("input.txt")
    total_amount_of_each_card = [1] * len(card_list)
    for index, card in enumerate(card_list):
        winning_card_list_string, numbers_to_match_list_string = _split_numbers(card)
        number_of_cards_won = _determine_card_score(
            winning_card_list_string, numbers_to_match_list_string
        )
        total_amount_of_each_card = _increment_next_n_card_totals(
            index + 1,
            total_amount_of_each_card,
            number_of_cards_won,
            total_amount_of_each_card[index],
        )

    print(_sum_total_cards_in_pile(total_amount_of_each_card))

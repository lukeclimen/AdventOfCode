# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are
# actually spelled out with letters: one, two, three, four, five, six, seven,
# eight, and nine also count as valid "digits".

import re
import typing


string_numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "\d",
]


def _convert_strings_to_ints(input_string: str) -> int:
    """Returns an integer from the string version of itself."""
    return string_numbers.index(input_string)


def _find_numbers_in_string(input_string: str) -> int:
    """Returns an integer from a string containing at least two digits"""

    number_list = re.findall(r"(?=({}))".format("|".join(string_numbers)), input_string)

    if number_list[0] in string_numbers:
        first_number = _convert_strings_to_ints(number_list[0]) * 10
    else:
        first_number = int(number_list[0]) * 10

    if number_list[-1] in string_numbers:
        second_number = _convert_strings_to_ints(number_list[-1])
    else:
        second_number = int(number_list[-1])

    return first_number + second_number


def sum_calibration_values(fileName: typing.Text) -> int:
    """Generates a calibration value from the calibration document."""

    file = open(fileName, "r")
    fileArr = file.read().split("\n")

    sum = 0
    for line in fileArr:
        sum += _find_numbers_in_string(line)

    return sum


if __name__ == "__main__":
    print("The calibration value is: ", sum_calibration_values("input.txt"))

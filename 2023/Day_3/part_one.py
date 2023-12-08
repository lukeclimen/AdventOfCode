# --- Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take
# you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not
# moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry,
#  I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a
#  while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody
# can figure out which one. If you can add up all the part numbers in the engine schematic,
# it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine.
# There are lots of numbers and symbols you don't really understand, but apparently any number
# adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
# (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, two numbers are not part numbers because they are not adjacent to a
# symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol
# and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part
# numbers in the engine schematic?

import re
import typing


def _sum_adjacent_part_numbers(index: int, line: str) -> int:
    """Returns the sum of any numbers that contain or are adjacent to the index."""
    sum = 0
    start_end_number_positions = [(m.span()) for m in re.finditer(r"[\d]+", line)]
    for positions in start_end_number_positions:
        if (
            (positions[0] <= index and index < positions[1] - 1)
            or (abs(positions[0] - index) <= 1)
            or (abs((positions[1] - 1) - index) <= 1)
        ):
            sum += int(line[positions[0] : positions[1]])
    return sum


def _find_symbol_indices(line: str) -> list[int]:
    """Returns the indices of any symbols found in a string"""
    return [(m.start(0)) for m in re.finditer(r"[^\w\.]", line)]


def sum_part_numbers(engine_schematic_list: list[str]) -> int:
    """Sums the part numbers according to the game description"""
    sum = 0
    previous_line = []
    current_line = []
    next_line = []
    for index, line in enumerate(engine_schematic_list):
        current_line = line
        current_line_symbol_positions = _find_symbol_indices(current_line)
        if len(current_line_symbol_positions) > 0:
            for symbol_position in current_line_symbol_positions:
                sum += _sum_adjacent_part_numbers(symbol_position, current_line)
                if index != 0:
                    previous_line = engine_schematic_list[index - 1]
                    sum += _sum_adjacent_part_numbers(symbol_position, previous_line)
                if index != len(engine_schematic_list) - 1:
                    next_line = engine_schematic_list[index + 1]
                    sum += _sum_adjacent_part_numbers(symbol_position, next_line)
    return sum


def _convert_file_into_array(file_name: typing.Text) -> list:
    """Converts text file into list of strings"""
    file = open(file_name, "r")
    file_list = file.read().split("\n")
    return file_list


if __name__ == "__main__":
    file_list = _convert_file_into_array("input.txt")
    print(sum_part_numbers(file_list))

# --- Part Two ---
# The engineer finds the missing part and installs it in the engine! As the engine springs
# to life, you jump in the closest gondola, finally ready to ascend to the water source.

# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately,
# the gondola has a phone labeled "help", so you pick it up and the engineer answers.

# Before you can explain the situation, she suggests that you look out the window. There
# stands the engineer, holding a phone in one hand and waving with the other. You're going
# so slowly that you haven't even left the station. You exit the gondola.

# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear
# is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the
# result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up so that the
# engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

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

# In this schematic, there are two gears. The first is in the top left; it has part numbers
# 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear
# ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one
# part number.) Adding up all of the gear ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?

import re
from part_one import _convert_file_into_array


def _get_adjacent_part_numbers(index: int, line: str) -> list[int]:
    """Returns a list of any numbers that contain or are adjacent to the index."""
    matching_numbers = []
    start_end_number_positions = [(m.span()) for m in re.finditer(r"[\d]+", line)]
    for positions in start_end_number_positions:
        if (
            (positions[0] <= index and index < positions[1] - 1)
            or (abs(positions[0] - index) <= 1)
            or (abs((positions[1] - 1) - index) <= 1)
        ):
            matching_numbers.append(int(line[positions[0] : positions[1]]))
    return matching_numbers


def _find_symbol_indices(line: str) -> list[int]:
    """Returns the indices of any '*' symbols found in a string"""
    return [(m.start(0)) for m in re.finditer(r"[*]", line)]


def sum_gear_ratios(engine_schematic_list: list[str]) -> int:
    """Sums the gear ratios according to the game description"""
    sum = 0
    previous_line = []
    current_line = []
    next_line = []
    for index, line in enumerate(engine_schematic_list):
        current_line = line
        current_line_symbol_positions = _find_symbol_indices(current_line)
        if len(current_line_symbol_positions) > 0:
            for symbol_position in current_line_symbol_positions:
                matching_gears = []
                matching_gears.extend(
                    _get_adjacent_part_numbers(symbol_position, current_line)
                )
                if index != 0:
                    previous_line = engine_schematic_list[index - 1]
                    matching_gears.extend(
                        _get_adjacent_part_numbers(symbol_position, previous_line)
                    )
                if index != len(engine_schematic_list) - 1:
                    next_line = engine_schematic_list[index + 1]
                    matching_gears.extend(
                        _get_adjacent_part_numbers(symbol_position, next_line)
                    )
                if len(matching_gears) > 1:
                    gear_ratio = 1
                    for gear in matching_gears:
                        gear_ratio *= gear
                    sum += gear_ratio
    return sum


if __name__ == "__main__":
    file_list = _convert_file_into_array("input.txt")
    print(sum_gear_ratios(file_list))

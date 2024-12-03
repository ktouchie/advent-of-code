import logging
import re
import sys

from aoc_2024.days.day03_part1 import get_sum_of_match_products, mul_pattern

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

command_pattern = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"


def get_matches_from_file(input_file):
    # Read the input file and return a list of regex matches
    with open(input_file, "r") as f:
        content = f.read()

    # Track whether mul is enabled
    mul_enabled = True
    mul_matches = []

    for match in re.finditer(command_pattern, content):
        if match.group() == "do()":
            mul_enabled = True
        elif match.group() == "don't()":
            mul_enabled = False
        elif match.group().startswith("mul") and mul_enabled:
            mul_matches += re.findall(mul_pattern, match.group())

    return mul_matches


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day03_part2.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    mul_matches = get_matches_from_file(input_file)
    get_sum_of_match_products(mul_matches)

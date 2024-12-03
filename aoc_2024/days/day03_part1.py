import logging
import re
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mul_pattern = r"(?:mul(\(\d{1,3}\,\d{1,3}\)))"


def get_matches_from_file(input_file):
    # Read the input file and return a list of regex matches
    with open(input_file, "r") as f:
        content = f.read()
    mul_matches = re.findall(mul_pattern, content)
    logger.info(f"Number of matches: {len(mul_matches)}")
    return mul_matches


def get_sum_of_match_products(mul_matches):
    # Initialize sum of products
    sum_of_products = 0
    # Get lists from matches and calculate the product
    for match in mul_matches:
        match_list = match[1:-1].split(",")
        sum_of_products += mul(match_list)
    # Log the sum of products
    logger.info(f"Sum of products: {sum_of_products}")
    return sum_of_products


def mul(match_list):
    return int(match_list[0]) * int(match_list[1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day03_part1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    matches = get_matches_from_file(input_file)
    get_sum_of_match_products(matches)

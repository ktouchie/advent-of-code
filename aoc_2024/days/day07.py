import itertools
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_file(input_file):
    # Read the input file and return a list of rows
    equations = {}
    with open(input_file, "r") as f:
        for line in f.readlines():
            values = line.split(":")
            test_value = int(values[0].strip())
            equations[test_value] = [int(x) for x in values[1].strip().split(" ")]
    logger.info(f"Equations: {equations}")
    return equations


def try_all_operators(equations):
    correct_test_values = set()
    for test_value, equation in equations.items():
        operator_combinations = list(
            itertools.product(operators, repeat=len(equation) - 1)
        )
        for operator_combination in operator_combinations:
            result = equation[0]
            for i in range(1, len(equation)):
                result = operator_combination[i - 1](result, equation[i])
            if result == test_value:
                correct_test_values.add(test_value)
                logger.info(f"For {test_value} = {equation}")
                logger.info(f"found successful combination: {operator_combination}")
                break
    logger.info(f"Correct test values: {correct_test_values}")
    logger.info(f"Sum of correct test values: {sum(correct_test_values)}")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


operators = [add, multiply]


def main(input_file):
    equations = parse_file(input_file)
    try_all_operators(equations)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day07.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)

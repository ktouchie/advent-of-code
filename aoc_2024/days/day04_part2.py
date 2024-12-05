import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

directions = [
    (-1, -1),  # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1),  # down-right
]


def get_grid_from_file(input_file):
    # Read the input file and return a list of rows
    with open(input_file, "r") as f:
        grid = [line.strip() for line in f.readlines()]
    return grid


def check_for_x_mas(row, col, grid):
    nb_rows = len(grid)
    nb_cols = len(grid[0])
    # Check all directions from 'A' are valid in grid
    for row_delta, col_delta in directions:
        if not (0 <= row + row_delta < nb_rows and 0 <= col + col_delta < nb_cols):
            return False
    # Start with upper left direction
    row_delta, col_delta = -1, -1
    # Check for 'MAS'
    if {
        grid[row + row_delta][col + col_delta],
        grid[row - row_delta][col - col_delta],
    } == {"M", "S"} and {
        grid[row - row_delta][col + col_delta],
        grid[row + row_delta][col - col_delta],
    } == {
        "M",
        "S",
    }:
        return True


def find_x_mas_in_grid(grid):
    found_words = 0
    # Iterate over every letter in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "A":
                if check_for_x_mas(row, col, grid):
                    found_words += 1

    logger.info(f"Found words: {found_words}")
    return found_words


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day04_part1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    grid = get_grid_from_file(input_file)
    find_x_mas_in_grid(grid)

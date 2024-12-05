import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

directions = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
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


def check_word_in_direction(row, col, row_delta, col_delta, word, grid):
    nb_rows = len(grid)
    nb_cols = len(grid[0])
    # Check for each letter in the word
    for i in range(len(word)):
        new_row = row + i * row_delta
        new_col = col + i * col_delta
        if new_row < 0 or new_row >= len(grid):
            return False
        # Check that next direction is in the grid
        if not (0 <= new_row < nb_rows and 0 <= new_col < nb_cols):
            return False
        # Check that the next letter is the same as the next letter in the word
        if grid[new_row][new_col] != word[i]:
            return False
    return True


def find_words_in_grid(grid, word):
    found_words = 0
    # Iterate over every letter in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for row_delta, col_delta in directions:
                if check_word_in_direction(row, col, row_delta, col_delta, word, grid):
                    found_words += 1

    logger.info(f"Found words: {found_words}")
    return found_words


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day04_part1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    grid = get_grid_from_file(input_file)
    word = "XMAS"
    find_words_in_grid(grid, word)

import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

guard_directions = {
    "^": (-1, 0),  # up
    ">": (0, 1),  # right
    "v": (1, 0),  # down
    "<": (0, -1),  # left
}


def get_grid_from_file(input_file):
    # Read the input file and return a list of rows
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid


def find_guard(grid):
    for row in range(len(grid)):
        guard_in_row = set(guard_directions.keys()).intersection(set(grid[row]))
        if guard_in_row:
            guard_direction = guard_in_row.pop()
            col = grid[row].index(guard_direction)
            logger.info(
                f"Guard found at row {row}, col {col}, direction {guard_direction}"
            )
            return row, col, guard_direction


def move_guard(row, col, direction):
    row_delta, col_delta = guard_directions[direction]
    return row + row_delta, col + col_delta


def turn_right(direction):
    if direction == "^":
        return ">"
    if direction == ">":
        return "v"
    if direction == "v":
        return "<"
    if direction == "<":
        return "^"


def mark_path(row, col, direction, grid, path=None):
    # Initialize path if it's the first time
    if path is None:
        path = {(row, col)}
    else:
        path.add((row, col))

    row_length = len(grid)
    col_length = len(grid[0])

    while True:
        # Move the guard in the current direction
        next_row, next_col = move_guard(row, col, direction)

        # Check if the next position is out of the grid
        if (
            next_row < 0
            or next_row >= row_length
            or next_col < 0
            or next_col >= col_length
        ):
            logger.info(f"Distinct positions visited: {len(path)}")
            return path

        # Check if the next position is an obstacle
        if grid[next_row][next_col] == "#":
            # Turn right and continue
            direction = turn_right(direction)
            return mark_path(row, col, direction, grid, path)

        path.add((next_row, next_col))
        row, col = next_row, next_col


def visualize_path(grid, path):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in path:
                print("X", end="")
            else:
                print(grid[row][col], end="")
        print()


def main(input_file):
    grid = get_grid_from_file(input_file)
    row, col, direction = find_guard(grid)
    path = mark_path(row, col, direction, grid)
    visualize_path(grid, path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day06_part1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)

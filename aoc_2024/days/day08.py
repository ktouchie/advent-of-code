import logging
import sys
from collections import defaultdict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_grid_from_file(input_file):
    # Read the input file and return a list of rows
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid


def parse_grid(grid):
    coordinates = defaultdict(list)
    for row in grid:
        for item in row:
            if not item == ".":
                # Add column and row to the coordinates
                coordinates[item].append((row.index(item), grid.index(row)))
    logger.info(f"Coordinates: {coordinates}")
    return coordinates


def calculate_antinode(pair1, pair2):
    col_distance = abs(pair2[0] - pair1[0])
    row_distance = abs(pair2[1] - pair1[1])

    antinode_col1 = (
        pair1[0] + col_distance if pair1[0] > pair2[0] else pair1[0] - col_distance
    )
    antinode_col2 = (
        pair2[0] + col_distance if pair2[0] > pair1[0] else pair2[0] - col_distance
    )

    antinode_row1 = (
        pair1[1] + row_distance if pair1[1] > pair2[1] else pair1[1] - row_distance
    )
    antinode_row2 = (
        pair2[1] + row_distance if pair2[1] > pair1[1] else pair2[1] - row_distance
    )

    return (antinode_row1, antinode_col1), (antinode_row2, antinode_col2)


def add_antinodes(coordinates, grid):
    antinodes = set()
    for _key, values in coordinates.items():
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                antinode1, antinode2 = calculate_antinode(values[i], values[j])

                if check_coordinate_validity(*antinode1, grid):
                    antinodes.add(antinode1)
                if check_coordinate_validity(*antinode2, grid):
                    antinodes.add(antinode2)
    logger.info(f"Antinodes: {antinodes}")
    logger.info(f"Number of antinodes: {len(antinodes)}")


def check_coordinate_validity(row, col, grid):
    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[0]):
        return False
    return True


def main(input_file):
    grid = get_grid_from_file(input_file)
    coordinates = parse_grid(grid)
    add_antinodes(coordinates, grid)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day06_part1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)

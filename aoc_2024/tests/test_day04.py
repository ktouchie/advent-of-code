import logging

import pytest

from aoc_2024.days.day04_part1 import check_word_in_direction, get_grid_from_file
from aoc_2024.utils import get_input_file_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


class TestDay04:

    @pytest.mark.parametrize(
        "input_file",
        [get_input_file_path("04_part1.txt")],
    )
    def test_get_lists_from_file(self, input_file):
        assert get_grid_from_file(input_file) == grid

    @pytest.mark.parametrize(
        "row, col, row_delta, col_delta, word, expected",
        [
            (1, 4, 0, 1, "XMAS", False),
            (1, 4, 1, 0, "XMAS", False),
            (1, 4, 1, 1, "XMAS", False),
            (1, 4, 1, -1, "XMAS", False),
            (1, 4, -1, 1, "XMAS", False),
            (1, 4, -1, -1, "XMAS", False),
            (1, 4, 0, -1, "XMAS", True),
            (1, 4, -1, 0, "XMAS", False),
        ],
    )
    def test_check_word_in_direction(
        self, row, col, row_delta, col_delta, word, expected
    ):
        assert (
            check_word_in_direction(row, col, row_delta, col_delta, word, grid)
            == expected
        )

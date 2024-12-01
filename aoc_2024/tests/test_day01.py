import logging

import pytest

from aoc_2024.days.day01 import (
    _count_occurrences,
    calculate_differences_sum,
    calculate_similarity_score,
)
from aoc_2024.utils import get_input_file_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestDay01:

    @pytest.mark.parametrize(
        "input_file",
        [get_input_file_path("01_part1.txt")],
    )
    def test_calculate_differences_sum(self, input_file):
        _, _, differences_sum = calculate_differences_sum(input_file)
        assert differences_sum == 11

    @pytest.mark.parametrize(
        "sorted_column, expected_output",
        [
            ([1, 2, 3, 3, 3, 4], {1: 1, 2: 1, 3: 3, 4: 1}),
            ([3, 3, 3, 4, 5, 9], {3: 3, 4: 1, 5: 1, 9: 1}),
        ],
    )
    def test_count_occurrences(self, sorted_column, expected_output):
        assert _count_occurrences(sorted_column) == expected_output

    def test_calculate_similarity_score(self):
        sorted_col1 = [1, 2, 3, 3, 3, 4]
        sorted_col2 = [3, 3, 3, 4, 5, 9]
        assert calculate_similarity_score(sorted_col1, sorted_col2) == 31

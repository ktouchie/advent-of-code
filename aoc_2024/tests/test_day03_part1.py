import logging

import pytest

from aoc_2024.days.day03_part1 import (
    get_matches_from_file,
    get_sum_of_match_products,
    mul,
)
from aoc_2024.utils import get_input_file_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestDay03Part1:

    @pytest.mark.parametrize(
        "input_file",
        [get_input_file_path("03_part1.txt")],
    )
    def test_get_matches_from_file(self, input_file):
        assert get_matches_from_file(input_file) == [
            "(2,4)",
            "(5,5)",
            "(11,8)",
            "(8,5)",
        ]

    def test_get_sum_of_match_products(self):
        assert get_sum_of_match_products(["(2,4)", "(5,5)", "(11,8)", "(8,5)"]) == 161

    def test_mul(self):
        assert mul(["2", "4"]) == 8
        assert mul(["5", "5"]) == 25
        assert mul(["11", "8"]) == 88
        assert mul(["8", "5"]) == 40

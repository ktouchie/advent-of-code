import logging

import pytest

from aoc_2024.days.day01 import Day01
from aoc_2024.utils import get_input_file_path

logger = logging.getLogger(__name__)


class TestDay01:

    @pytest.mark.parametrize(
        "input_file",
        [get_input_file_path("01_part1.txt")],
    )
    def test_calculate_differences_sum(self, input_file):
        day01 = Day01(input_file)
        assert day01.calculate_differences_sum() == 11

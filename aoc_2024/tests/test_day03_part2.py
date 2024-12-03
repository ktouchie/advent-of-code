import logging

import pytest

from aoc_2024.days.day03_part2 import get_matches_from_file
from aoc_2024.utils import get_input_file_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestDay03Part1:

    @pytest.mark.parametrize(
        "input_file",
        [get_input_file_path("03_part2.txt")],
    )
    def test_get_matches_from_file(self, input_file):
        assert get_matches_from_file(input_file) == [
            "(2,4)",
            "(8,5)",
        ]

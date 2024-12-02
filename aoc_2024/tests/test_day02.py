import logging

import pytest

from aoc_2024.days.day02 import (
    check_difference,
    check_list_progression,
    check_list_safety,
    get_lists_from_file,
)
from aoc_2024.utils import get_input_file_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

lists = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


class TestDay02:

    @pytest.mark.parametrize(
        "input_file",
        [get_input_file_path("02_part1.txt")],
    )
    def test_get_lists_from_file(self, input_file):
        assert get_lists_from_file(input_file) == lists

    @pytest.mark.parametrize(
        "first, second, ascending, expected_result",
        [
            (1, 3, True, True),
            (5, 3, False, True),
            (4, 4, True, False),
            (7, 8, False, False),
            (3, 5, True, True),
            (8, 6, False, True),
            (1, 5, True, False),
        ],
    )
    def test_check_difference(self, first, second, ascending, expected_result):
        assert check_difference(first, second, ascending) == expected_result

    @pytest.mark.parametrize(
        "report_list, ascending, expected_result",
        [
            (lists[0], False, 1),
            (lists[1], True, 0),
            (lists[2], False, 0),
            (lists[3], True, 0),
            (lists[4], False, 0),
            (lists[5], True, 1),
        ],
    )
    def test_check_list_progression(self, report_list, ascending, expected_result):
        assert check_list_progression(report_list, ascending) == expected_result

    def test_check_list_safety(self):
        assert check_list_safety(lists) == 2

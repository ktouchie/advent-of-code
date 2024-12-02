import logging

import pytest
from pytest_mock import MockerFixture

from aoc_2024.days.day02 import (
    check_difference,
    check_list_progression,
    check_list_safety,
    get_lists_from_file,
    is_safe,
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
            (lists[0], False, True),
            (lists[1], True, False),
            (lists[2], False, False),
            (lists[3], True, False),
            (lists[4], False, False),
            (lists[5], True, True),
        ],
    )
    def test_check_list_progression(
        self, mocker: MockerFixture, report_list, ascending, expected_result
    ):
        mocker.patch(
            "aoc_2024.days.day02.check_difference", return_value=expected_result
        )
        assert check_list_progression(report_list, ascending) == expected_result

    @pytest.mark.parametrize(
        "report_list, expected_result",
        [
            (lists[0], True),
            (lists[1], False),
            (lists[2], False),
            (lists[3], True),
            (lists[4], True),
            (lists[5], True),
        ],
    )
    def test_is_safe(self, mocker: MockerFixture, report_list, expected_result):
        mocker.patch(
            "aoc_2024.days.day02.check_list_progression", return_value=expected_result
        )
        assert is_safe(report_list) == expected_result

    def test_check_list_safety(self):
        assert check_list_safety(lists) == 4

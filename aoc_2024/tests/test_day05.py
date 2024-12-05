import logging

import pytest

from aoc_2024.days.day05 import (
    get_lists_from_file,
    get_middle_page,
    get_sum_of_middle_pages,
    printing_order_respects_rule,
)
from aoc_2024.utils import get_input_file_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestDay05:

    @pytest.mark.parametrize(
        "input_file",
        [get_input_file_path("05_part1.txt")],
    )
    def test_get_lists_from_file(self, input_file):
        assert get_lists_from_file(input_file) == (
            [
                [47, 53],
                [97, 13],
                [97, 61],
                [97, 47],
                [75, 29],
                [61, 13],
                [75, 53],
                [29, 13],
                [97, 29],
                [53, 29],
                [61, 53],
                [97, 53],
                [61, 29],
                [47, 13],
                [75, 47],
                [97, 75],
                [47, 61],
                [75, 61],
                [47, 29],
                [75, 13],
                [53, 13],
            ],
            [
                [75, 47, 61, 53, 29],
                [97, 61, 53, 29, 13],
                [75, 29, 13],
                [75, 97, 47, 61, 53],
                [61, 13, 29],
                [97, 13, 75, 29, 47],
            ],
        )

    def test_printing_order_respects_rule(self):
        assert printing_order_respects_rule([47, 53], [75, 47, 61, 53, 29])
        assert printing_order_respects_rule([97, 13], [75, 47, 61, 53, 29])
        assert not printing_order_respects_rule([29, 13], [61, 13, 29])

    def test_get_middle_page(self):
        assert get_middle_page([75, 47, 61, 53, 29]) == 61
        assert get_middle_page([97, 61, 53, 29, 13]) == 53
        assert get_middle_page([75, 29, 13]) == 29

    @pytest.mark.parametrize(
        "input_file",
        [get_input_file_path("05_part1.txt")],
    )
    def test_get_sum_of_middle_pages(self, input_file):
        assert get_sum_of_middle_pages(input_file) == (143, 123)

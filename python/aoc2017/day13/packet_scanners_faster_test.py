from aoc2017.day13.packet_scanners_test import EXAMPLE_ONE, MODEL_ONE
from packet_scanners_faster import *


def test_parse():
    assert parse(EXAMPLE_ONE) == MODEL_ONE


def test_part_one():
    assert part_one(MODEL_ONE) == 24


def test_part_two():
    assert part_two(MODEL_ONE) == 10

from .packet_scanners import *

EXAMPLE_ONE = """0: 3
1: 2
4: 4
6: 4"""

MODEL_ONE = [3, 2, None, None, 4, None, 4]


def test_parse():
    assert parse(EXAMPLE_ONE) == MODEL_ONE


def test_part_one():
    assert part_one(MODEL_ONE) == 24


def test_part_two():
    assert part_two(MODEL_ONE) == 10

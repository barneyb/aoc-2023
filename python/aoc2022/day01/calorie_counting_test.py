from calorie_counting import *

EXAMPLE_ONE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

MODEL_ONE = (10_000, 11_000, 24_000)


def test_parse():
    assert parse(EXAMPLE_ONE) == MODEL_ONE


def test_part_one():
    assert part_one(MODEL_ONE) == 24_000


def test_part_two():
    assert part_two(MODEL_ONE) == 45_000

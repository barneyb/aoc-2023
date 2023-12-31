from .wait_for_it import *

# fmt: off
EXAMPLE = """Time:      7  15   30
Distance:  9  40  200
"""

MODEL = [( 7,   9),
         (15,  40),
         (30, 200),
        ]
# fmt: on


def test_parse_many():
    assert parse_many(EXAMPLE) == MODEL


def test_ways_to_win():
    assert ways_to_win(*MODEL[0]) == len([2, 3, 4, 5])
    assert ways_to_win(*MODEL[1]) == len([4, 5, 6, 7, 8, 9, 10, 11])
    assert ways_to_win(*MODEL[2]) == len([11, 12, 13, 14, 15, 16, 17, 18, 19])


def test_example_one():
    assert part_one(EXAMPLE) == 288


def test_example_two():
    assert part_two(EXAMPLE) == 71503

from .mirage_maintenance import *

# fmt: off
EXAMPLE = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

MODEL = [[ 0,  3,  6,  9, 12, 15],
         [ 1,  3,  6, 10, 15, 21],
         [10, 13, 16, 21, 30, 45],
        ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_extrapolate():
    assert extrapolate(MODEL[0]) == (-3, 18)
    assert extrapolate(MODEL[1]) == (0, 28)
    assert extrapolate(MODEL[2]) == (5, 68)


def test_example_one():
    assert part_one(MODEL) == 114


def test_example_two():
    assert part_two(MODEL) == 2

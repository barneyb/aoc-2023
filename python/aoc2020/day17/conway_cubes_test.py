from conway_cubes import *

# fmt: off
EXAMPLE = """.#.
..#
###
"""

MODEL = {(1, 0),
         (2, 1),
         (0, 2),
         (1, 2),
         (2, 2)}
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_example_one():
    assert part_one(MODEL, cycles=0) == 5
    assert part_one(MODEL, cycles=1) == 11
    assert part_one(MODEL, cycles=2) == 21
    assert part_one(MODEL, cycles=3) == 38
    assert part_one(MODEL) == 112


def test_example_two():
    assert part_two(MODEL) == 848

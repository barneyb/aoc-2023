from hill_climbing_algorithm import *

# fmt: off
EXAMPLE = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

# dims, start, end, map
MODEL = (8, 5), (0, 0), (5, 2), ["aabqponm",
                                 "abcryxxl",
                                 "accszzxk",
                                 "acctuvwj",
                                 "abdefghi"]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_example_one():
    assert part_one(MODEL) == 31

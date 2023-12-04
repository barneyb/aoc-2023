from hill_climbing_algorithm import *

# fmt: off
EXAMPLE = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

MAP = Map(EXAMPLE)
# fmt: on


def test_parse():
    assert MAP.width == 8
    assert MAP.height == 5
    assert MAP.start == (0, 0)
    assert MAP.end == (5, 2)
    assert str(MAP) == EXAMPLE


def test_example_one():
    assert part_one(MAP) == 31


def test_example_two():
    assert part_two(MAP) == 29

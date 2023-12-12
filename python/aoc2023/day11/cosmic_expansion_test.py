from .cosmic_expansion import *

# fmt: off
EXAMPLE = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
# fmt: on

MODEL = parse(EXAMPLE)


def test_part_one():
    assert part_one(MODEL) == 374


def test_other_factors():
    assert either_part(MODEL, 2) == 374
    assert either_part(MODEL, 10) == 1030
    assert either_part(MODEL, 100) == 8410

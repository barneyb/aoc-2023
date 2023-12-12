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

MODEL = [(4, 0),
         (9, 1),
         (0, 2),
         (8, 5),
         (1, 6),
         (12, 7),
         (9, 10),
         (0, 11),
         (5, 11),
         ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    assert part_one(MODEL) == 374


# def test_part_two():
#     assert part_two(MODEL) == 1_234

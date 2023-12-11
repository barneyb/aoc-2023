from .settlers_of_the_north_pole import *

# fmt: off
EXAMPLE = """\
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.
"""

MODEL = (10, 10, [".#.#...|#.",
                  ".....#|##|",
                  ".|..|...#.",
                  "..|#.....#",
                  "#.#|||#|#|",
                  "...#.||...",
                  ".|....|...",
                  "||...#|.#|",
                  "|.||||..|.",
                  "...#.|..|.",
                 ])
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    assert part_one(MODEL) == 1147

from subterranean_sustainability import *

# The three 'die off' notes are not part of the raw example
EXAMPLE = """initial state: #..#.#..##......###...###

...## => #
....# => .
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
##### => .
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
..... => .
"""

MODEL = (
    "#..#.#..##......###...###",
    {
        "...##",
        "..#..",
        ".#...",
        ".#.#.",
        ".#.##",
        ".##..",
        ".####",
        "#.#.#",
        "#.###",
        "##.#.",
        "##.##",
        "###..",
        "###.#",
        "####.",
    },
)


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    assert part_one(MODEL) == 325

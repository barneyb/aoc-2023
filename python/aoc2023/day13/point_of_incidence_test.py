from .point_of_incidence import *

# fmt: off
EXAMPLE = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

MODEL = [["#.##..##.",
          "..#.##.#.",
          "##......#",
          "##......#",
          "..#.##.#.",
          "..##..##.",
          "#.#.##.#.",
         ],
         ["#...##..#",
          "#....#..#",
          "..##..###",
          "#####.##.",
          "#####.##.",
          "..##..###",
          "#....#..#",
         ],
        ]

MODEL_TWO = [
    [
        "#..#.#........#",
        "#..######..####",
        ".##..#.#.##.#.#",
        "#..##..........",
        "######........#",
        "#..####......##",
        ".##.##.#...##.#",
    ]
]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_rotate_cw():
    assert rotate_cw(["123", "456"]) == ["41", "52", "63"]


def test_vert_line():
    assert vert_line(MODEL[0]) == 5
    assert vert_line(MODEL[1]) == -1
    assert vert_line(MODEL_TWO[0]) == 2


def test_horiz_line():
    assert horiz_line(MODEL[0]) == -1
    assert horiz_line(MODEL[1]) == 4


def test_part_one():
    assert part_one(MODEL) == 405


# def test_part_two():
#     assert part_two(MODEL) == 1_234

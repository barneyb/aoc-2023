from .parabolic_reflector_dish import *

# fmt: off
EXAMPLE = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

PARSE_EXAMPLE="""\
O.#
#OO
"""
PARSE_MODEL = (3, 2, {(0, 0): "O",
                      (2, 0): "#",
                      (0, 1): "#",
                      (1, 1): "O",
                      (2, 1): "O",
                     })
# fmt: on

MODEL = parse(EXAMPLE)


def test_parse():
    assert parse(PARSE_EXAMPLE) == PARSE_MODEL
    assert unparse(PARSE_MODEL) == PARSE_EXAMPLE


def test_part_one():
    assert part_one(MODEL) == 136


# def test_part_two():
#     assert part_two(MODEL) == 1_234

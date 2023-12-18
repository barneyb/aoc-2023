from .lavaduct_lagoon import *

# fmt: off
EXAMPLE = """\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

MODEL = [(1, 6, "#70c710"),
         (2, 5, "#0dc571"),
         (3, 2, "#5713f0"),
         (2, 2, "#d2c081"),
         (1, 2, "#59c680"),
         (2, 2, "#411b91"),
         (3, 5, "#8ceee2"),
         (0, 2, "#caa173"),
         (3, 1, "#1b58a2"),
         (0, 2, "#caa171"),
         (1, 2, "#7807d2"),
         (0, 3, "#a77fa3"),
         (3, 2, "#015232"),
         (0, 2, "#7a21e3"),
        ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    assert part_one(MODEL) == 62


# def test_part_two():
#     assert part_two(MODEL) == 1_234

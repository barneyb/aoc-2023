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

MODEL_TWO = [(1, 461937),
             (2, 56407),
             (1, 356671),
             (2, 863240),
             (1, 367720),
             (2, 266681),
             (3, 577262),
             (0, 829975),
             (3, 112010),
             (2, 829975),
             (3, 491645),
             (0, 686074),
             (3, 5411),
             (0, 500254),
            ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    assert part_one(MODEL) == 62


def test_parse_color():
    assert parse_color("#70c710") == (1, 461937)
    assert parse_color("#0dc571") == (2, 56407)
    assert parse_color("#5713f0") == (1, 356671)
    assert parse_color("#d2c081") == (2, 863240)
    assert parse_color("#59c680") == (1, 367720)
    assert parse_color("#411b91") == (2, 266681)
    assert parse_color("#8ceee2") == (3, 577262)
    assert parse_color("#caa173") == (0, 829975)
    assert parse_color("#1b58a2") == (3, 112010)
    assert parse_color("#caa171") == (2, 829975)
    assert parse_color("#7807d2") == (3, 491645)
    assert parse_color("#a77fa3") == (0, 686074)
    assert parse_color("#015232") == (3, 5411)
    assert parse_color("#7a21e3") == (0, 500254)


def test_reparse():
    assert reparse(MODEL) == MODEL_TWO


def test_part_two():
    assert part_two(MODEL) == 952408144115

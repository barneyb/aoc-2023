from .never_tell_me_the_odds import *

# fmt: off
EXAMPLE = """\
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

MODEL = [((19, 13, 30), (-2,  1, -2)),
         ((18, 19, 22), (-1, -1, -2)),
         ((20, 25, 34), (-2, -2, -4)),
         ((12, 31, 28), (-1, -2, -1)),
         ((20, 19, 15), ( 1, -5, -3)),
        ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    assert part_one(MODEL, 7, 27) == 2


# def test_part_two():
#     assert part_two(MODEL) == 1_234

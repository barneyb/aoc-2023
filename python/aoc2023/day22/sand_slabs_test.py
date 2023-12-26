from .sand_slabs import *

# fmt: off
EXAMPLE = """\
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

MODEL = [((1, 2), (0, 3), (1, 2)),
         ((0, 3), (0, 1), (2, 3)),
         ((0, 3), (2, 3), (3, 4)),
         ((0, 1), (0, 3), (4, 5)),
         ((2, 3), (0, 3), (5, 6)),
         ((0, 3), (1, 2), (6, 7)),
         ((1, 2), (1, 2), (8, 10)),
        ]
# fmt: on


def test_parse_brick():
    assert parse_brick("0,0,10~1,0,10") == ((0, 2), (0, 1), (10, 11))


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    assert part_one(MODEL) == 5


def test_part_two():
    assert part_two(MODEL) == 7

from .pipe_maze import *

# fmt: off
EXAMPLE_ONE = """\
-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

EXAMPLE_TWO = """\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""
# fmt: on


def test_parse():
    m = Map(EXAMPLE_ONE)
    assert m.cols == 5
    assert m.rows == 5
    assert m.start == (1, 1)
    assert m[(1, 1)] == "F"


def test_example_one():
    assert part_one(Map(EXAMPLE_ONE)) == 4
    assert part_one(Map(EXAMPLE_TWO)) == 8


# def test_example_two():
#     assert part_two(MODEL) == 1_234

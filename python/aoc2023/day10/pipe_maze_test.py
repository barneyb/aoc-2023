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

EXAMPLE_THREE = """\
OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
"""

EXAMPLE_FOUR = """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
# fmt: on


def test_parse():
    m = Map(EXAMPLE_ONE)
    assert m.cols == 5
    assert m.rows == 5
    assert m.start == (1, 1)
    assert m[(1, 1)] == "F"


def test_part_one():
    assert part_one(Map(EXAMPLE_ONE)) == 4
    assert part_one(Map(EXAMPLE_TWO)) == 8


def test_part_two():
    assert part_two(Map(EXAMPLE_THREE)) == 8
    assert part_two(Map(EXAMPLE_FOUR)) == 10

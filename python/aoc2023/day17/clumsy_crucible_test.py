from .clumsy_crucible import *

# fmt: off
EXAMPLE_ONE = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

EXAMPLE_TWO = """\
111111111111
555599995551
555599995551
555599995551
555599999991
"""

PARSE_EXAMPLE = """\
2413
3215
"""

PARSE_MODEL = (4, 2, [[2, 4, 1, 3],
                      [3, 2, 1, 5],
                      ])
# fmt: on
MODEL_ONE = Map(EXAMPLE_ONE)
MODEL_TWO = Map(EXAMPLE_TWO)


def test_parse():
    m = Map(PARSE_EXAMPLE)
    assert m.width == 4
    assert m.height == 2
    assert m.start == (0, 0)
    assert m.goal == (3, 1)
    assert m.layout == [
        [2, 4, 1, 3],
        [3, 2, 1, 5],
    ]


def test_part_one():
    assert part_one(MODEL_ONE) == 102
    assert part_one(MODEL_TWO) == 47


def test_part_two():
    assert part_two(MODEL_ONE) == 94
    assert part_two(MODEL_TWO) == 71

from .clumsy_crucible import *

# fmt: off
EXAMPLE = """\
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

PARSE_EXAMPLE="""\
2413
3215
"""

PARSE_MODEL = (4, 2, [[2, 4, 1, 3],
                      [3, 2, 1, 5],
                      ])
# fmt: on
MODEL = parse(EXAMPLE)


def test_parse():
    assert parse(PARSE_EXAMPLE) == PARSE_MODEL


def test_part_one():
    assert part_one(MODEL) == 102


# def test_part_two():
#     assert part_two(MODEL) == 1_234

from .science_for_hungry_people import *

# fmt: off
EXAMPLE = """\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""

MODEL = [[-1, -2,  6,  3, 8],
         [ 2,  3, -2, -1, 3],
        ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_multiply():
    assert multiply(5, MODEL[0]) == [-5, -10, 30, 15, 40]


def test_add():
    assert add([1, 2], [5, 6]) == [6, 8]


def test_get_options():
    a, b, c = [[1], [10], [100]]
    assert list(get_options(3, [a, b, c])) == [
        [[0], [0], [300]],
        [[0], [10], [200]],
        [[0], [20], [100]],
        [[0], [30], [0]],
        [[1], [0], [200]],
        [[1], [10], [100]],
        [[1], [20], [0]],
        [[2], [0], [100]],
        [[2], [10], [0]],
        [[3], [0], [0]],
    ]


def test_example_one():
    assert part_one(MODEL) == 62842880


# def test_example_two():
#    assert part_two(MODEL) == 1_234

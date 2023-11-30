from space_image_format import *

EXAMPLE = """123456789012"""

MODEL = [[[1, 2, 3], [4, 5, 6]],
         [[7, 8, 9], [0, 1, 2]]]


def test_parse():
    assert parse(EXAMPLE, 3, 2) == MODEL


def test_example_one():
    assert part_one(MODEL) == 1

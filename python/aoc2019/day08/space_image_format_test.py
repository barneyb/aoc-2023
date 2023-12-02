from space_image_format import *

EXAMPLE_ONE = "123456789012"

MODEL_ONE = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [0, 1, 2]],
]

EXAMPLE_TWO = "0222112222120000"


def test_parse():
    assert parse(EXAMPLE_ONE, 3, 2) == MODEL_ONE


def test_example_one():
    assert part_one(MODEL_ONE) == 1


def test_example_two():
    model = parse(EXAMPLE_TWO, 2, 2)
    assert (
        part_two(model)
        == """ #
# """
    )

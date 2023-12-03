from chronal_calibration import *

# fmt: off
EXAMPLE = """+1
-2
+3
+1"""

MODEL = [1, -2, 3, 1]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_example_one():
    assert part_one(MODEL) == 3


def test_example_two():
    assert part_two(MODEL) == 2

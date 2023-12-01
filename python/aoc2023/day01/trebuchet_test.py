from trebuchet import *

EXAMPLE = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

MODEL = ["12", "38", "15", "77"]


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_example_one():
    assert part_one(MODEL) == 142

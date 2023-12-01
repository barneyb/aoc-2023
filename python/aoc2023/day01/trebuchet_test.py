from trebuchet import *

EXAMPLE_ONE = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EXAMPLE_TWO = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def test_example_one():
    assert part_one(EXAMPLE_ONE) == 142


def test_example_two():
    assert part_two(EXAMPLE_TWO) == 281


def test_overlap():
    assert part_two("twone") == 21

from gear_ratios import *

EXAMPLE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

MODEL = Schematic(EXAMPLE)


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_find_symbols():
    symbols = MODEL.find_symbols()
    assert symbols.keys() == {"*", "#", "+", "$"}
    assert symbols["*"] == [(3, 1), (3, 4), (5, 8)]
    assert symbols["#"] == [(6, 3)]


def test_example_1a():
    assert part_one(MODEL) == 4361


def test_example_1b():
    assert part_two(MODEL) == 467835

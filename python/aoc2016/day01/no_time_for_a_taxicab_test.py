from .no_time_for_a_taxicab import *

PATH_ONE = [("R", 2), ("L", 3)]


def test_parse():
    assert list(parse("R2, L3")) == PATH_ONE


def test_part_one():
    assert part_one(PATH_ONE) == 5


def test_part_two():
    path = parse("R8, R4, R4, R8")
    assert part_two(path) == 4

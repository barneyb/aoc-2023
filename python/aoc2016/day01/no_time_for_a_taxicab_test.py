from no_time_for_a_taxicab import *

PATH_ONE = [('R', 2), ('L', 3)]


def test_parse():
    assert PATH_ONE == parse("R2, L3")


def test_part_one():
    assert 5 == part_one(PATH_ONE)


def test_part_two():
    path = parse("R8, R4, R4, R8")
    assert 4 == part_two(path)

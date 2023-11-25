from no_time_for_a_taxicab import *

MODEL_ONE = [('R', 2), ('L', 3)]


def test_parse():
    assert MODEL_ONE == parse("R2, L3")


def test_part_one():
    assert 5 == part_one(MODEL_ONE)

from .clumsy_crucible_test import EXAMPLE_ONE, EXAMPLE_TWO, PARSE_EXAMPLE
from .clumsy_graph import *

MODEL_ONE = Graph(EXAMPLE_ONE)
MODEL_TWO = Graph(EXAMPLE_TWO)


def test_parse():
    g = Graph(PARSE_EXAMPLE)
    assert g.goal == 7


def test_part_one1():
    assert part_one(MODEL_ONE) == 102


def test_part_one2():
    assert part_one(MODEL_TWO) == 47


def test_part_two1():
    assert part_two(MODEL_ONE) == 94


def test_part_two2():
    assert part_two(MODEL_TWO) == 71

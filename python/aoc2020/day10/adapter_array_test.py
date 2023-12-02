from adapter_array import *

EXAMPLE_ONE = """16
10
15
5
1
11
7
19
6
12
4
"""

MODEL_ONE = [
    1,
    4,
    5,
    6,
    7,
    10,
    11,
    12,
    15,
    16,
    19,
]


def test_parse():
    assert parse(EXAMPLE_ONE) == MODEL_ONE


def test_example_one():
    assert part_one(MODEL_ONE) == 35

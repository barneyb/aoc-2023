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

EXAMPLE_TWO = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

MODEL_TWO = parse(EXAMPLE_TWO)


def test_parse():
    assert parse(EXAMPLE_ONE) == MODEL_ONE


def test_example_1a():
    assert part_one(MODEL_ONE) == 35


def test_example_1b():
    assert part_one(MODEL_TWO) == 220


def test_example_2a():
    assert part_two(MODEL_ONE) == 8


def test_example_2b():
    assert part_two(MODEL_TWO) == 19208

from .haunted_wasteland import *

# fmt: off
EXAMPLE_ONE = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

MODEL_ONE = ("RL",
             {"AAA": ("BBB", "CCC"),
              "BBB": ("DDD", "EEE"),
              "CCC": ("ZZZ", "GGG"),
              "DDD": ("DDD", "DDD"),
              "EEE": ("EEE", "EEE"),
              "GGG": ("GGG", "GGG"),
              "ZZZ": ("ZZZ", "ZZZ"),
             })

EXAMPLE_TWO = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

MODEL_TWO = ("LLR",
             {"AAA": ("BBB", "BBB"),
              "BBB": ("AAA", "ZZZ"),
              "ZZZ": ("ZZZ", "ZZZ"),
             })
# fmt: on


def test_parse():
    assert parse(EXAMPLE_ONE) == MODEL_ONE
    assert parse(EXAMPLE_TWO) == MODEL_TWO


def test_over_and_over():
    itr = iter(over_and_over("abc"))
    assert next(itr) == "a"
    assert next(itr) == "b"
    assert next(itr) == "c"
    assert next(itr) == "a"
    assert next(itr) == "b"
    assert next(itr) == "c"
    assert next(itr) == "a"


def test_example_one():
    assert part_one(MODEL_ONE) == 2


def test_example_two():
    assert part_one(MODEL_TWO) == 6


# def test_example_two():
#    assert part_two(MODEL) == 3

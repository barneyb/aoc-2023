from .haunted_wasteland import *

# fmt: off
EXAMPLE_1A = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

MODEL_1A = ("RL",
            {"AAA": ("BBB", "CCC"),
             "BBB": ("DDD", "EEE"),
             "CCC": ("ZZZ", "GGG"),
             "DDD": ("DDD", "DDD"),
             "EEE": ("EEE", "EEE"),
             "GGG": ("GGG", "GGG"),
             "ZZZ": ("ZZZ", "ZZZ"),
            })

EXAMPLE_1B = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

MODEL_1B = ("LLR",
            {"AAA": ("BBB", "BBB"),
             "BBB": ("AAA", "ZZZ"),
             "ZZZ": ("ZZZ", "ZZZ"),
            })

EXAMPLE_2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

MODEL_2 = ("LR",
           {"11A": ("11B", "XXX"),
            "11B": ("XXX", "11Z"),
            "11Z": ("11B", "XXX"),
            "22A": ("22B", "XXX"),
            "22B": ("22C", "22C"),
            "22C": ("22Z", "22Z"),
            "22Z": ("22B", "22B"),
            "XXX": ("XXX", "XXX"),
           })
# fmt: on


def test_parse():
    assert parse(EXAMPLE_1A) == MODEL_1A
    assert parse(EXAMPLE_1B) == MODEL_1B
    assert parse(EXAMPLE_2) == MODEL_2


def test_over_and_over():
    itr = iter(over_and_over("abc"))
    assert next(itr) == "a"
    assert next(itr) == "b"
    assert next(itr) == "c"
    assert next(itr) == "a"
    assert next(itr) == "b"
    assert next(itr) == "c"
    assert next(itr) == "a"


def test_example_1a():
    assert part_one(MODEL_1A) == 2


def test_example_1b():
    assert part_one(MODEL_1B) == 6


def test_example_2():
    assert part_two(MODEL_2) == 6

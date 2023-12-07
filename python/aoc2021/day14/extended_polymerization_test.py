from .extended_polymerization import *

# fmt: off
EXAMPLE = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

MODEL = ("N",
         Counter(["NN", "NC", "CB"]),
         {"CH": "B",
          "HH": "N",
          "CB": "H",
          "NH": "C",
          "HB": "C",
          "HC": "B",
          "HN": "C",
          "NN": "C",
          "BH": "H",
          "NC": "B",
          "NB": "B",
          "BN": "B",
          "BB": "N",
          "BC": "B",
          "CC": "N",
          "CN": "C"})
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_example_one():
    assert part_one(MODEL) == 1588


# def test_example_two():
#    assert part_two(MODEL) == 3

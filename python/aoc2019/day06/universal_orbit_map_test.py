from .universal_orbit_map import *

# fmt: off
EXAMPLE_ONE = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

EXAMPLE_TWO = f"""{EXAMPLE_ONE}
K)YOU
I)SAN"""

MODEL_ONE = {"COM": [],
             "B": ["B"],
             "G": ["G", "B"],
             "H": ["H", "G", "B"],
             "C": ["C", "B"],
             "D": ["D", "C", "B"],
             "I": ["I", "D", "C", "B"],
             "E": ["E", "D", "C", "B"],
             "J": ["J", "E", "D", "C", "B"],
             "K": ["K", "J", "E", "D", "C", "B"],
             "L": ["L", "K", "J", "E", "D", "C", "B"],
             "F": ["F", "E", "D", "C", "B"]}

MODEL_TWO = {"YOU": ["YOU", *MODEL_ONE["K"]],
             "SAN": ["SAN", *MODEL_ONE["I"]], }
MODEL_TWO.update(MODEL_ONE)
# fmt: on


def test_parse():
    assert parse(EXAMPLE_ONE) == MODEL_ONE
    assert parse(EXAMPLE_TWO) == MODEL_TWO


def test_example_one():
    assert part_one(MODEL_ONE) == 42


def test_example_two():
    assert part_two(MODEL_TWO) == 4

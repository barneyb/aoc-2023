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
K)L
"""

EXAMPLE_TWO = f"""{EXAMPLE_ONE}
K)YOU
I)SAN
"""

MODEL_ONE = [("B", "COM"),
             ("C", "B"),
             ("D", "C"),
             ("E", "D"),
             ("F", "E"),
             ("G", "B"),
             ("H", "G"),
             ("I", "D"),
             ("J", "E"),
             ("K", "J"),
             ("L", "K"), ]

MODEL_TWO = [*MODEL_ONE,
             ("YOU", "K"),
             ("SAN", "I"), ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE_ONE) == MODEL_ONE


def test_example_one():
    assert part_one(MODEL_ONE) == 42


def test_example_two():
    assert part_two(MODEL_TWO) == 4

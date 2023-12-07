from .universal_orbit_map import *

# fmt: off
EXAMPLE = """COM)B
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

MODEL = [("COM", "B"),
         ("B", "C"),
         ("C", "D"),
         ("D", "E"),
         ("E", "F"),
         ("B", "G"),
         ("G", "H"),
         ("D", "I"),
         ("E", "J"),
         ("J", "K"),
         ("K", "L"),]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_example_one():
    assert part_one(MODEL) == 42


# def test_example_two():
#    assert part_two(MODEL) == 3

from cube_conundrum import *

# fmt: off
EXAMPLE_ZERO = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

MODEL_ZERO = [(1, [(4, 0, 3),
                   (1, 2, 6),
                   (0, 2, 0)]),
              ]

EXAMPLE = f"""{EXAMPLE_ZERO}
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
# fmt: on


def test_parse():
    assert parse(EXAMPLE_ZERO) == MODEL_ZERO


def test_part_one():
    model = parse(EXAMPLE)
    assert part_one(model) == 8

from .step_counter import *

# fmt: off
EXAMPLE = """\
so
many
lines
"""

MODEL = ["so", 
         "many", 
         "lines",
        ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    assert part_one(MODEL) == 7_654


# def test_part_two():
#     assert part_two(MODEL) == 1_234

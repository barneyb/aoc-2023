from .the_floor_will_be_lava import *

# fmt: off
EXAMPLE = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

PARSE_EXAMPLE=r""".-\
|/.
"""

PARSE_MODEL=(3, 2, {(1, 0): "-",
                    (2, 0): "\\",
                    (0, 1): "|",
                    (1, 1): "/",
                    })
# fmt: on

MODEL = parse(EXAMPLE)


def test_parse():
    assert parse(PARSE_EXAMPLE) == PARSE_MODEL
    assert len(set(len(l) for l in EXAMPLE.splitlines())) == 1


def test_part_one():
    assert part_one(MODEL) == 46


def test_part_two():
    assert part_two(MODEL) == 51

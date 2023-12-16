from .lens_library import *

# fmt: off
EXAMPLE = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

MODEL = ["rn=1",
         "cm-",
         "qp=3",
         "cm=2",
         "qp-",
         "pc=4",
         "ot=9",
         "ab=5",
         "pc-",
         "pc=6",
         "ot=7",
        ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


# noinspection PyPep8Naming
def test_HASH():
    assert HASH("HASH") == 52
    assert HASH("rn=1") == 30
    assert HASH("cm-") == 253
    assert HASH("qp=3") == 97
    assert HASH("cm=2") == 47
    assert HASH("qp-") == 14
    assert HASH("pc=4") == 180
    assert HASH("ot=9") == 9
    assert HASH("ab=5") == 197
    assert HASH("pc-") == 48
    assert HASH("pc=6") == 214
    assert HASH("ot=7") == 231


def test_part_one():
    assert part_one(MODEL) == 1320


# def test_part_two():
#     assert part_two(MODEL) == 1_234

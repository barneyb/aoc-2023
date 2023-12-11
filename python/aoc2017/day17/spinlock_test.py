from .spinlock import *


def test_part_one():
    assert part_one(3, 7) == 2
    assert part_one(3) == 638


def test_part_two():
    assert part_two(3, 8) == 5

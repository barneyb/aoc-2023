from .not_quite_lisp import *


def test_part_one():
    assert part_one("(()(()(") == 3
    assert part_one("())") == -1


def test_part_two():
    assert part_two("()())") == 5

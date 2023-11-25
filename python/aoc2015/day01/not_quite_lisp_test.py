from not_quite_lisp import *


def test_part_one():
    assert 3 == part_one("(()(()(")
    assert -1 == part_one("())")


def test_part_two():
    assert 5 == part_two("()())")

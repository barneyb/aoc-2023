from not_quite_lisp import *


def test_both_parts():
    a, b = both_parts("(()(()(")
    assert a == 3
    a, b = both_parts("())")
    assert a == -1
    a, b = both_parts("()())")
    assert b == 5

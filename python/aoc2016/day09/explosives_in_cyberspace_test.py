from explosives_in_cyberspace import *


def test_example_1():
    assert part_one("ADVENT") == 6


def test_example_2():
    assert part_one("A(1x5)BC") == 7


def test_example_3():
    assert part_one("(3x3)XYZ") == 9


def test_example_4():
    assert part_one("A(2x2)BCD(2x2)EFG") == 11


def test_example_5():
    assert part_one("(6x1)(1x3)A") == 6


def test_example_6():
    assert part_one("X(8x2)(3x3)ABCY") == 18

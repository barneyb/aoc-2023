from .explosives_in_cyberspace import *


def test_example_1_1():
    assert part_one("ADVENT") == 6


def test_example_1_2():
    assert part_one("A(1x5)BC") == 7


def test_example_1_3():
    assert part_one("(3x3)XYZ") == 9


def test_example_1_4():
    assert part_one("A(2x2)BCD(2x2)EFG") == 11


def test_example_1_5():
    assert part_one("(6x1)(1x3)A") == 6


def test_example_1_6():
    assert part_one("X(8x2)(3x3)ABCY") == 18


def test_example_2_1():
    assert part_two("(3x3)XYZ") == len("XYZXYZXYZ")


def test_example_2_2():
    assert part_two("X(8x2)(3x3)ABCY") == len("XABCABCABCABCABCABCY")


def test_example_2_3():
    assert part_two("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920


def test_example_2_4():
    assert part_two("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445

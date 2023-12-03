from inverse_captcha import *


def test_examples_1():
    assert part_one("1122") == 3
    assert part_one("1111") == 4
    assert part_one("1234") == 0
    assert part_one("91212129") == 9

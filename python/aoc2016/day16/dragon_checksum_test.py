from .dragon_checksum import *


def test_gen():
    assert gen("1") == "100"
    assert gen("0") == "001"
    assert gen("11111") == "11111000000"
    assert gen("111100001010") == "1111000010100101011110000"


def test_chksum():
    assert chksum("110010110100") == "100"
    assert chksum("10000011110010000111") == "01100"


def test_example_one():
    assert fill_and_chksum("10000", 20) == "01100"

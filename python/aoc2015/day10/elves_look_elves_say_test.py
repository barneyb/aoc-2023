from aoc2015.day10.elves_look_elves_say import *


def test_example_one():
    assert look_and_say("1") == "11"


def test_example_two():
    assert look_and_say("11") == "21"


def test_example_three():
    assert look_and_say("21") == "1211"


def test_example_four():
    assert look_and_say("1211") == "111221"


def test_example_five():
    assert look_and_say("111221") == "312211"

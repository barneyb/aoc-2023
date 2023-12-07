from .camel_cards import *

# fmt: off
EXAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

MODEL = [("32T3K", 765),
         ("T55J5", 684),
         ("KK677", 28),
         ("KTJJT", 220),
         ("QQQJA", 483),
        ]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_get_hand_type():
    assert get_hand_type("AAAAA") == Hand.FIVE
    assert get_hand_type("AA8AA") == Hand.FOUR
    assert get_hand_type("23332") == Hand.FULL_HOUSE
    assert get_hand_type("TTT98") == Hand.THREE
    assert get_hand_type("23432") == Hand.TWO_PAIR
    assert get_hand_type("A23A4") == Hand.PAIR
    assert get_hand_type("23456") == Hand.HIGH


def test_get_card_strengths():
    assert get_card_strengths("AKQJT") == [14, 13, 12, 11, 10]
    assert get_card_strengths("9876") == [9, 8, 7, 6]
    assert get_card_strengths("5432") == [5, 4, 3, 2]


def test_get_hand_strength():
    assert get_hand_strength("TTT98") == [Hand.THREE, 10, 10, 10, 9, 8]


def test_strength_comparison():
    assert get_hand_strength("TTT98") < get_hand_strength("TTT9Q")
    assert get_hand_strength("TTT98") > get_hand_strength("89TTT")


def test_example_one():
    assert part_one(MODEL) == 6440


# def test_example_two():
#    assert part_two(MODEL) == 3

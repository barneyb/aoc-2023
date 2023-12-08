from collections import Counter
from enum import IntEnum

from util import aoc


class Hand(IntEnum):
    HIGH = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE = 4
    FULL_HOUSE = 5
    FOUR = 6
    FIVE = 7


def parse(input):
    return [(ls, int(b)) for ls, b in (l.split(" ") for l in input.splitlines())]


def get_hand_type(labels):
    hist = Counter(labels)
    counts = set(hist.values())
    match len(hist):
        case 1:
            return Hand.FIVE
        case 2 if 4 in counts:
            return Hand.FOUR
        case 2 if 2 in counts or 3 in counts:
            return Hand.FULL_HOUSE
        case 3 if 3 in counts:
            return Hand.THREE
        case 3 if 2 in counts:
            return Hand.TWO_PAIR
        case 4:
            return Hand.PAIR
        case 5:
            return Hand.HIGH
        case _:
            raise RuntimeError(f"No type for hand '{labels}'")


def get_card_strengths(labels):
    return ["23456789TJQKA".index(l) + 2 for l in labels]


def get_card_strengths_jokers(labels):
    return ["J23456789T_QKA".index(l) + 1 for l in labels]


def get_hand_strength(labels):
    return [get_hand_type(labels), *get_card_strengths(labels)]


def get_hand_type_jokers(labels):
    natural = get_hand_type(labels)
    if "J" in labels:
        cs = set(labels)
        if len(cs) != 1:
            return max(get_hand_type(labels.replace("J", c)) for c in cs if c != "J")
    return natural


def get_hand_strength_jokers(labels):
    return [get_hand_type_jokers(labels), *get_card_strengths_jokers(labels)]


def either_part(model, get_hs):
    pairs = sorted((get_hs(ls), b) for ls, b in model)
    return sum((i + 1) * b for i, (_, b) in enumerate(pairs))


def part_one(model):
    return either_part(model, get_hand_strength)


def part_two(model):
    return either_part(model, get_hand_strength_jokers)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

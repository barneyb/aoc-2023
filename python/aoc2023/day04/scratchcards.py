import re

from util import aoc

RE_SPACES = re.compile(r"\s+")


def parse(input):
    result = []
    for line in input.splitlines():
        win, have = [
            [int(n) for n in RE_SPACES.split(ns.strip())]
            for ns in line.split(":")[1].split("|")
        ]
        result.append((set(win), have))
    return result


def points(card):
    win, have = card
    return sum(1 if h in win else 0 for h in have)


def part_one(model):
    return sum(2 ** (p - 1) for p in (points(card) for card in model) if p > 0)


def part_two(model):
    copies = [1] * len(model)
    for i, card in enumerate(model):
        for n in range(points(card)):
            copies[i + n + 1] += copies[i]
    return sum(copies)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

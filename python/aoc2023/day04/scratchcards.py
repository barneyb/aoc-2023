import re

from util import aoc

RE_SPACES = re.compile("\s+")


def parse(input):
    result = []
    for line in input.splitlines():
        win, have = [
            [int(n) for n in RE_SPACES.split(ns.strip())]
            for ns in line.split(":")[1].split("|")
        ]
        result.append((set(win), have))
    return result


def part_one(model):
    total = 0
    for win, have in model:
        n = sum(1 if h in win else 0 for h in have)
        if n > 0:
            total += 2 ** (n - 1)
    return total


def part_two(model):
    copies = [1] * len(model)
    for i, (win, have) in enumerate(model):
        for n in range(sum(1 if h in win else 0 for h in have)):
            copies[i + n + 1] += copies[i]
    return sum(copies)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

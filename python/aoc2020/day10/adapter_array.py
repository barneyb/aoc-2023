from collections import Counter

from util import aoc


def parse(input):
    return sorted(int(j) for j in input.splitlines())


def part_one(model):
    hist = Counter()
    hist[3] = 1  # last adapter -> device
    prev = 0
    for j in model:
        hist[j - prev] += 1
        prev = j
    return hist[1] * hist[3]


def part_two(model):
    hist = Counter()
    hist[0] = 1  # the charge port
    for adapter in model:
        for jlt in range(adapter - 3, adapter):
            hist[adapter] += hist[jlt]
    return hist[model[-1]]


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

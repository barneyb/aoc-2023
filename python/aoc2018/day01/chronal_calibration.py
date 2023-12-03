import operator
from functools import reduce

from util import aoc


def parse(input):
    return [int(n.strip()) for n in input.splitlines()]


def part_one(model):
    return reduce(operator.add, model, 0)


def part_two(changes):
    freqs = set()
    f = 0
    while True:
        for d in changes:
            f += d
            if f in freqs:
                return f
            freqs.add(f)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

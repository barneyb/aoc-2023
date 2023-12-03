import operator
from functools import reduce

from util import aoc


def parse(input):
    return [int(n.strip()) for n in input.splitlines()]


def part_one(model):
    return reduce(operator.add, model, 0)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
    )

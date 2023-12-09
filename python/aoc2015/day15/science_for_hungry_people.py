import operator
import re
from functools import reduce

from util import aoc

RE_PARSE = re.compile(
    r"[^:]+: \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+)"
)


def parse(input):
    return [
        [int(m.group(i)) for i in range(1, 6)]
        for m in (RE_PARSE.fullmatch(l) for l in input.splitlines())
    ]


def multiply(s, v):
    return [s * e for e in v]


def add(a, b):
    return [n + m for n, m in zip(a, b)]


def get_options(tsp, ings):
    ing, *rest = ings
    if not len(rest):
        yield [multiply(tsp, ing)]
        return
    for t in range(tsp + 1):
        for opts in get_options(tsp - t, rest):
            yield [multiply(t, ing)] + opts


def part_one(ings):
    cookies = [reduce(add, o) for o in get_options(100, ings)]
    scores = [reduce(operator.mul, c[:4]) for c in cookies if all(n > 0 for n in c)]
    return max(scores)


# def part_two(model):
#    return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

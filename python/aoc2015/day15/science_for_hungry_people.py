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


def get_recipes(tsp, ings):
    ing, *rest = ings
    if not len(rest):
        yield [multiply(tsp, ing)]
        return
    for t in range(tsp + 1):
        for opts in get_recipes(tsp - t, rest):
            yield [multiply(t, ing)] + opts


def either_part(ings, accept=None):
    recipes = (reduce(add, o) for o in get_recipes(100, ings))
    if accept:
        recipes = filter(accept, recipes)
    recipes = filter(lambda r: all(n > 0 for n in r), recipes)
    return max(reduce(operator.mul, r[:4]) for r in recipes)


def part_one(ings):
    return either_part(ings)


def part_two(ings):
    return either_part(ings, lambda r: r[4] == 500)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

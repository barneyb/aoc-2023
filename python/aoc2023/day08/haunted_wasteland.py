import math
import re

from util import aoc

# AAA = (BBB, BBB)
RE_MAP = re.compile(r"(\S+)\s*=\s*\(([^,]+),\s*([^)]+)\)")


def parse(input):
    turns, _, *lines = input.splitlines()
    entries = [
        (m.group(1), (m.group(2), m.group(3))) for m in (RE_MAP.match(l) for l in lines)
    ]
    return turns, dict(entries)


def over_and_over(iterable):
    while True:
        yield from iterable


def path_len(model, start, is_end):
    turns, maps = model
    maps = dict(maps)
    curr = start
    i = 0
    for d in over_and_over(turns):
        i += 1
        curr = maps[curr][0 if d == "L" else 1]
        if is_end(curr):
            return i


def part_one(model):
    return path_len(model, "AAA", lambda c: c == "ZZZ")


def part_two(model):
    _, maps = model
    lengths = [
        path_len(model, k, lambda s: s.endswith("Z"))
        for k in maps.keys()
        if k.endswith("A")
    ]
    return math.lcm(*lengths)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

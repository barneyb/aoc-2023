import re
from functools import reduce

from util import aoc

RE_MAP = re.compile(r"(\w+)-to-(\w+) map")


def parse_ints(s):
    return tuple(int(s) for s in s.strip().split(" "))


def parse(input):
    seeds = None
    mappings = {}
    for block in input.split("\n\n"):
        if block.startswith("seeds:"):
            seeds = parse_ints(block.split(":")[1])
            continue
        first, *lines = block.splitlines()
        s, d = RE_MAP.match(first).groups()
        ms = [parse_ints(l) for l in lines]
        mappings[s] = (d, sorted(ms, key=lambda t: t[1]))
    return seeds, mappings


def convert(n, mapping):
    type, ms = mapping
    for d, s, r in ms:
        if s <= n < s + r:
            return d + (n - s)
    return n  # unchanged


def linearize(mappings):
    src = "seed"
    ordered = []
    while src != "location":
        for s in mappings:
            if s == src:
                src, ms = mappings[s]
                ordered.append((src, ms))
                break
    assert len(ordered) == len(mappings)
    return ordered


def to_location(seed, mappings):
    return reduce(convert, mappings, seed)


def part_one(model):
    seeds, mappings = model
    mappings = linearize(mappings)
    return min(to_location(s, mappings) for s in seeds)


# def part_two(model):
#    return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

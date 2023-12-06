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


def convert_one(window, mapping):
    n, _ = window
    tgt, ms = mapping
    for d, s, r in ms:
        if s <= n < s + r:
            n = d + (n - s)
            break
    return [(n, n + 1)]


def convert(windows, mapping):
    result = []
    for w in windows:
        result.extend(convert_one(w, mapping))
    return result


def to_locations(windows, mappings):
    return reduce(convert, mappings, windows)


def a_part(pairs, mappings):
    mappings = linearize(mappings)
    return min(m for m, _ in to_locations(pairs, mappings))


def part_one(model):
    seeds, mappings = model
    return a_part([(s, s + 1) for s in seeds], mappings)


def part_two(model):
    seeds, mappings = model
    return a_part([(s, s + r) for s, r in zip(seeds[::2], seeds[1::2])], mappings)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

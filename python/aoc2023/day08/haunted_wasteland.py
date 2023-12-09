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


def part_one(model):
    turns, maps = model
    map = dict(maps)
    curr = "AAA"
    i = 0
    for d in over_and_over(turns):
        i += 1
        curr = map[curr][0 if d == "L" else 1]
        if curr == "ZZZ":
            return i


# def part_two(model):
#    return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

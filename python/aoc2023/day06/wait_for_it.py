import re

from util import aoc

RE_SPACES = re.compile(r"\s+")


def parse_many(input):
    return list(
        zip(
            *[
                [int(n) for n in RE_SPACES.split(l.split(":")[1].strip())]
                for l in input.splitlines()
            ]
        )
    )


def ways_to_win(time, dist):
    n = 0
    for t in range(time):
        if t * (time - t) > dist:
            n += 1
    return n


def part_one(input):
    total = 1
    for t, d in parse_many(input):
        total *= ways_to_win(t, d)
    return total


def part_two(input):
    t, d = [int(RE_SPACES.sub("", l.split(":")[1])) for l in input.splitlines()]
    return ways_to_win(t, d)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        None,
        part_one,
        part_two,
    )

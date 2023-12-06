import re

from util import aoc

RE_SPACES = re.compile(r"\s+")


def parse(input):
    return list(
        zip(
            *[
                [int(n) for n in RE_SPACES.split(l.split(":")[1].strip())]
                for l in input.splitlines()
            ]
        )
    )


def ways_to_win(time, dist):
    ds = []
    for t in range(time):
        if t * (time - t) > dist:
            ds.append(t)
    return ds


def part_one(model):
    total = 1
    for t, d in model:
        total *= len(ways_to_win(t, d))
    return total


# def part_two(model):
#    return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

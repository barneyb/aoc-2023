import functools

from util import aoc


def parse(input):
    return [
        (ss, tuple(int(g) for g in gs.split(",")))
        for ss, gs in (l.split(" ") for l in input.splitlines())
    ]


def arrangements(row):
    @functools.cache
    def arrs(item):
        gs, idx = item
        while idx < ss_len and springs[idx] == ".":
            idx += 1
        if idx >= ss_len:
            return 1 if not len(gs) else 0
        if not len(gs):
            return 1 if "#" not in springs[idx:] else 0
        g = gs[0]
        n = 0
        end = idx + g
        if (end <= ss_len and "." not in springs[idx:end]) and (
            end == ss_len or springs[end] != "#"
        ):
            n += arrs((gs[1:], idx + g + 1))
        if springs[idx] == "?":
            n += arrs((gs, idx + 1))
        return n

    springs, groups = row
    ss_len = len(springs)
    return arrs((groups, 0))


def part_one(model):
    return sum(map(arrangements, model))


def unfold(row):
    springs, groups = row
    return "?".join([springs] * 5), groups * 5


def part_two(model):
    return sum(map(arrangements, map(unfold, model)))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

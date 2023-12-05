import functools

from util import aoc


def parse(input):
    points = set()
    for y, line in enumerate(input.splitlines()):
        for p in ((x, y) for x, c in enumerate(line) if c == "#"):
            points.add(p)
    return points


def cartesian_product(ranges):
    def helper(basis, rs):
        this_range, *others = rs
        if len(others) == 0:
            for d in this_range:
                yield *basis, d
        else:
            for d in this_range:
                yield from helper((*basis, d), others)

    yield from helper((), ranges)


@functools.cache
def neighbors(p):
    return list(
        filter(
            lambda n: n != p,  # sorta silly :)
            cartesian_product([range(d - 1, d + 2) for d in p]),
        )
    )


def tick(points):
    to_check = set()
    for p in points:
        to_check.update(neighbors(p))

    state = set()
    for p in to_check:
        active_neighbors = sum(1 for n in neighbors(p) if n in points)
        if active_neighbors == 3:
            state.add(p)
        elif active_neighbors == 2:
            if p in points:
                state.add(p)
    return state


def part_one(model, cycles=6):
    state = set((*p, 0) for p in model)
    for _ in range(cycles):
        state = tick(state)
    return len(state)


def part_two(model):
    state = set((*p, 0, 0) for p in model)
    for _ in range(6):
        state = tick(state)
    return len(state)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

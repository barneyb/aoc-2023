from util import aoc


def parse(input):
    return int(input)


def part_one(step_size, iterations=2017):
    ns = [0]
    idx = 0
    for i in range(iterations):
        idx = (idx + step_size) % len(ns) + 1
        ns.insert(idx, i + 1)
    return ns[idx + 1]


def part_two(step_size, iterations=50_000_000):
    l = 1
    idx = 0
    az = 0
    for i in range(1, iterations):
        idx = (idx + step_size) % l + 1
        if idx == 1:
            az = i
        l += 1
    return az


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

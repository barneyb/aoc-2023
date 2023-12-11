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


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

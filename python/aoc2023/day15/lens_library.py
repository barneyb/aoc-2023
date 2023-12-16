from util import aoc


def parse(input):
    return input.strip().split(",")


# noinspection PyPep8Naming
def HASH(s):
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h


def part_one(steps):
    return sum(HASH(s) for s in steps)


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

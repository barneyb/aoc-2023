from util import aoc


def part_one(input):
    floor = 0
    i = 0
    for c in input:
        i += 1
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            raise RuntimeError("Unknown '" + c + "'")
    return floor


def part_two(input):
    floor = 0
    i = 0
    for c in input:
        i += 1
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            raise RuntimeError("Unknown '" + c + "'")
        if floor == -1:
            return i
    raise RuntimeError("Never entered basement")


if __name__ == "__main__":
    aoc.solve(
        __file__,
        None,
        part_one,
        part_two,
    )

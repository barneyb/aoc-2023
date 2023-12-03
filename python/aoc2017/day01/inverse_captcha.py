from util import aoc


def part_one(s):
    prev = s[-1]
    sum = 0
    for c in s:
        if c == prev:
            sum += int(c)
        prev = c
    return sum


if __name__ == "__main__":
    aoc.solve(
        __file__,
        None,
        part_one,
    )

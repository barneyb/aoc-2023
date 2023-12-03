from util import aoc


def part_one(s):
    prev = s[-1]
    sum = 0
    for c in s:
        if c == prev:
            sum += int(c)
        prev = c
    return sum


def part_two(s):
    sum = 0
    l = len(s)
    half = l // 2
    for i, c in enumerate(s):
        if c == s[(i + half) % l]:
            sum += int(c)
    return sum


if __name__ == "__main__":
    aoc.solve(
        __file__,
        None,
        part_one,
        part_two,
    )

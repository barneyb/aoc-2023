from util import aoc


def parse(input):
    a, b, c = 0, 0, 0
    curr = 0
    for line in input.splitlines():
        if line == "":
            a, b, c = largest_three(a, b, c, curr)
            curr = 0
        else:
            curr += int(line)
    a, b, c = largest_three(a, b, c, curr)
    return a, b, c


def largest_three(a, b, c, d):
    if d < b:
        if d < a:
            return a, b, c
        return d, b, c
    if d < c:
        return b, d, c
    return b, c, d


def part_one(three):
    return three[2]


def part_two(three):
    return sum(three)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

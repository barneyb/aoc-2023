from util import aoc


def part_one(input):
    best = 0
    curr = 0
    for line in input.splitlines():
        if line == "":
            best = max(curr, best)
            curr = 0
        else:
            curr += int(line)
    return max(curr, best)


def part_two(input):
    def doit(a, b, c, d):
        if d < a:
            return a, b, c
        if d < b:
            return d, b, c
        if d < c:
            return b, d, c
        return b, c, d

    a, b, c = 0, 0, 0
    curr = 0
    for line in input.splitlines():
        if line == "":
            a, b, c = doit(a, b, c, curr)
            curr = 0
        else:
            curr += int(line)
    a, b, c = doit(a, b, c, curr)
    return a + b + c


if __name__ == "__main__":
    aoc.solve(__file__,
              None,
              part_one,
              part_two)

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


if __name__ == "__main__":
    aoc.solve(__file__,
              None,
              part_one)

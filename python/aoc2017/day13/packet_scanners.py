from util import aoc


def parse(input):
    ranges = []
    for line in input.splitlines():
        lyr, rng = [int(s) for s in line.split(": ")]
        deficiency = lyr - len(ranges) + 1
        if deficiency > 0:
            ranges.extend([None for _ in range(deficiency)])
        ranges[lyr] = rng
    return ranges


def part_one(ranges):
    lyr = 0
    severity = 0
    for rng in ranges:
        if rng is not None and lyr % (rng + rng - 2) == 0:
            severity += lyr * rng
        lyr += 1
    return severity


if __name__ == "__main__":
    aoc.solve(__file__,
              parse,
              part_one)

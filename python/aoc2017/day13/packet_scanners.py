import itertools

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
    severity = 0
    for lyr, rng in get_layers_caught(ranges, 0):
        severity += lyr * rng
    return severity


def get_layers_caught(ranges, delay):
    lyr = 0
    tick = delay
    for rng in ranges:
        if rng is not None and (lyr + tick) % (rng + rng - 2) == 0:
            yield lyr, rng
        lyr += 1


def part_two(ranges):
    for delay in itertools.count():
        try:
            next(get_layers_caught(ranges, delay))
        except StopIteration:
            # never got caught!
            return delay


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

import re

from util import aoc

RE_FIRST = re.compile(r"\D*(\d)")
RE_LAST = re.compile(r"(\d)\D*$")


def parse(input):
    nums = []
    for line in input.splitlines():
        f = RE_FIRST.match(line)
        l = RE_LAST.search(line)
        nums.append(f.group(1) + l.group(1))
    return nums


def part_one(model):
    return sum(int(n) for n in model)


if __name__ == "__main__":
    aoc.solve(__file__,
              parse,
              part_one)

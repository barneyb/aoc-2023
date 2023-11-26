import re

from util import aoc

RE_ABBA = re.compile(r"(.)(.)\2\1")


def parse(input):
    return [parse_addr(addr) for addr in input.splitlines()]


def parse_addr(addr):
    other, hyper = [], []
    for i, p in enumerate(re.split("[][]", addr.strip())):
        if not p:
            continue
        if i % 2 == 0:
            other.append(p)
        else:
            hyper.append(p)
    return other, hyper


def has_abba(parts):
    for p in parts:
        m = RE_ABBA.search(p)
        if m and m.group(1) != m.group(2):
            return True
    return False


def part_one(addrs):
    count = 0
    for other, hyper in addrs:
        if has_abba(other) and not has_abba(hyper):
            count += 1
    return count


if __name__ == "__main__":
    aoc.solve(__file__,
              parse,
              part_one)

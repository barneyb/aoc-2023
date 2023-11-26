import re

from util import aoc

RE_NETS = re.compile("[][]")
RE_ABBA = re.compile(r"(.)(.)\2\1")
RE_ABA = re.compile(r"(.)(.)\1")


def parse(input):
    return (parse_addr(addr) for addr in input.splitlines())


def parse_addr(line):
    super, hyper = [], []
    for i, p in enumerate(RE_NETS.split(line.strip())):
        if not p:
            continue
        if i % 2 == 0:
            super.append(p)
        else:
            hyper.append(p)
    return super, hyper


def has_abba(parts):
    for p in parts:
        m = RE_ABBA.search(p)
        if m and m.group(1) != m.group(2):
            return True
    return False


def part_one(addrs):
    count = 0
    for a in addrs:
        if supports_tls(a):
            count += 1
    return count


def supports_tls(addr):
    super, hyper = addr
    return has_abba(super) and not has_abba(hyper)


def get_abas(parts):
    for p in parts:
        start = 0
        while start < len(p) - 2:
            m = RE_ABA.search(p, start)
            if m and m.group(1) != m.group(2):
                yield m.group()
                start = m.start()
            start += 1


def supports_ssl(addr):
    super, hyper = addr
    for aba in get_abas(super):
        bab = aba[1] + aba[0:2]
        for p in hyper:
            if bab in p:
                return True
    return False


def part_two(addrs):
    count = 0
    for a in addrs:
        if supports_ssl(a):
            count += 1
    return count


if __name__ == "__main__":
    aoc.solve(__file__,
              parse,
              part_one,
              part_two)

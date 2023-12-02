import re

from util import aoc

RE_MARKER = re.compile(r"\((\d+)x(\d+)\)")


def part_one(input):
    return decompressed_length(input, 0, len(input), lambda inpt, s, e, sl: e - s)


def decompressed_length(input, start, end, sub_length):
    decomp_len = 0
    while start < end:
        m = RE_MARKER.search(input, start, end)
        if m is None:
            decomp_len += end - start
            break
        decomp_len += m.start() - start
        l = int(m.group(1))
        start = m.end() + l
        l = sub_length(input, m.end(), m.end() + l, sub_length)
        n = int(m.group(2))
        decomp_len += l * n
    return decomp_len


def part_two(input):
    return decompressed_length(input, 0, len(input), decompressed_length)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        None,
        part_one,
        part_two,
    )

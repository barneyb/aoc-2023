import re

from util import aoc

RE_MARKER = re.compile(r"\((\d+)x(\d+)\)")


def part_one(input):
    comp_len = len(input)
    decomp_len = 0
    pos = 0
    while pos < comp_len:
        m = RE_MARKER.search(input, pos)
        if m is None:
            decomp_len += comp_len - pos
            break
        decomp_len += m.start() - pos
        l = int(m.group(1))
        pos = m.end() + l
        n = int(m.group(2))
        decomp_len += l * n
    return decomp_len


def decompressed_length(input, start, end):
    decomp_len = 0
    while start < end:
        m = RE_MARKER.search(input, start, end)
        if m is None:
            decomp_len += end - start
            break
        decomp_len += m.start() - start
        l = int(m.group(1))
        start = m.end() + l
        l = decompressed_length(input, m.end(), m.end() + l)
        n = int(m.group(2))
        decomp_len += l * n
    return decomp_len


def part_two(input):
    return decompressed_length(input, 0, len(input))


if __name__ == "__main__":
    aoc.solve(__file__,
              None,
              part_one,
              part_two)

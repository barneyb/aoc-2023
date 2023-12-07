import re

from aoc2016.day08.screen import Screen
from util import aoc, block_print

RE_RECT = re.compile(r"(rect) (\d+)x(\d+)")
RE_COL = re.compile(r"rotate (col)umn x=(\d+) by (-?\d+)")
RE_ROW = re.compile(r"rotate (row) y=(\d+) by (-?\d+)")


def parse(input):
    return [parse_line(l) for l in input.splitlines()]


def parse_line(line):
    m = RE_RECT.match(line)
    if not m:
        m = RE_COL.match(line)
    if not m:
        m = RE_ROW.match(line)
    if not m:
        raise RuntimeError(f"Unmatchable: '{line}'")
    return (m.group(1), int(m.group(2)), int(m.group(3)))


def both_parts(instructions):
    screen = Screen(50, 6)
    screen.execute(instructions)
    return screen.lit_pixel_count(), block_print.read(str(screen))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        both_parts,
    )

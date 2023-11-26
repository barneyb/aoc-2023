import re

from util import aoc

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
    return (m.group(1),
            int(m.group(2)),
            int(m.group(3)))


def part_one(instructions):
    return lit_pixel_count(
        build_and_execute(instructions, 50, 6))


def lit_pixel_count(display):
    return sum(1 if p else 0 for p in display)


def build_and_execute(instructions, width, height):
    display = new_display(width, height)
    return execute(display, instructions, width, height)


def execute(display, instructions, width, height):
    display_len = len(display)

    def xytoi(x, y):
        while x < 0:
            x += width
        x %= width
        while y < 0:
            y += display_len
        y %= height
        i = y * width + x
        assert 0 <= i < display_len
        return i % display_len

    def itoxy(i):
        return i % width, i // width

    def munge(i, dx, dy):
        x, y = itoxy(i)
        return xytoi(x + dx, y + dy)

    for ins, a, b in instructions:
        match ins:
            case 'rect':
                display = [True if i % width < a and i // width < b else p
                           for i, p in enumerate(display)]
            case 'row':
                display = [display[munge(i, -b, 0)] if i // width == a else p
                           for i, p in enumerate(display)]
            case 'col':
                display = [display[munge(i, 0, -b)] if i % width == a else p
                           for i, p in enumerate(display)]
                pass
    return display


def new_display(width, height):
    return [False] * (width * height)


def to_string(display, width, height):
    pixels = []
    for y in range(height):
        if y > 0:
            pixels.append("\n")
        row = y * width
        for x in range(width):
            pixels.append("#" if display[row + x] else ".")
    return "".join(pixels)


if __name__ == "__main__":
    aoc.solve(__file__,
              parse,
              part_one)

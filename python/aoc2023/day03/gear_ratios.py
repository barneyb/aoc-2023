from util import aoc


def parse(input):
    schematic = input.splitlines()
    w = len(schematic[0])
    h = len(schematic)
    return w, h, schematic


def find_symbols(schematic):
    symbols = {}
    for y, line in enumerate(schematic):
        for x, c in enumerate(line):
            if c == "." or c.isdigit():
                continue
            if c not in symbols:
                symbols[c] = []
            symbols[c].append((x, y))
    return symbols


def neighbors(p, w, h):
    x, y = p
    return filter(
        lambda p: 0 <= p[0] < w and 0 <= p[1] < h,
        [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x - 1, y),
        ],
    )


def num_bound(string, start, delta):
    pos = start
    l = len(string)
    while 0 <= pos < l and string[pos].isdigit():
        pos += delta
    # we went one too far
    return pos - delta


def part_one(model):
    w, h, schematic = model
    symbols = find_symbols(schematic)

    number_locations = set()
    for ps in symbols.values():
        for p in ps:
            for x, y in neighbors(p, w, h):
                if not schematic[y][x].isdigit():
                    continue
                x = num_bound(schematic[y], x, -1)
                number_locations.add((x, y))

    total = 0
    for x, y in number_locations:
        total += int(schematic[y][x : num_bound(schematic[y], x, 1) + 1])
    return total


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
    )

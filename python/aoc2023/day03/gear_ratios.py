from util import aoc
from util.linear_grid import LinearGrid, parse_chars


def parse(input):
    return parse_chars(input)


def part_one(model):
    w, h, schematic = model
    grid = LinearGrid(w, h, schematic)
    digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    number_locations = set()
    for i, c in enumerate(schematic):
        if c == "." or c in digits:
            continue
        for p in grid.neighbors(grid.to_point(i)):
            if not grid.in_bounds(p):
                continue
            if grid[p] not in digits:
                continue
            # scan left for the start of the number
            while True:
                x, y = p
                n = (x - 1, y)
                if grid[n] not in digits:
                    break
                p = n
            number_locations.add(p)
    total = 0
    for p in number_locations:
        num = 0
        while True:
            num = num * 10 + int(grid[p])
            x, y = p
            n = (x + 1, y)
            if grid[n] not in digits:
                break
            p = n
        total += num
    return total


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
    )

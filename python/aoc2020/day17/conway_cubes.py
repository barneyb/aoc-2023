from util import aoc


def parse(input):
    points = set()
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                points.add((x, y, 0))  # arbitrarily choosing z=0
    return points


def neighbors(x, y, z):
    return [
        (x - 1, y - 1, z - 1),
        (x, y - 1, z - 1),
        (x + 1, y - 1, z - 1),
        (x + 1, y, z - 1),
        (x + 1, y + 1, z - 1),
        (x, y + 1, z - 1),
        (x - 1, y + 1, z - 1),
        (x - 1, y, z - 1),
        (x, y, z - 1),
        (x - 1, y - 1, z),
        (x, y - 1, z),
        (x + 1, y - 1, z),
        (x + 1, y, z),
        (x + 1, y + 1, z),
        (x, y + 1, z),
        (x - 1, y + 1, z),
        (x - 1, y, z),
        (x - 1, y - 1, z + 1),
        (x, y - 1, z + 1),
        (x + 1, y - 1, z + 1),
        (x + 1, y, z + 1),
        (x + 1, y + 1, z + 1),
        (x, y + 1, z + 1),
        (x - 1, y + 1, z + 1),
        (x - 1, y, z + 1),
        (x, y, z + 1),
    ]


def tick(points):
    xr = yr = zr = 0, 0
    for p in points:
        x, y, z = p
        xr = min(xr[0], x - 1), max(xr[1], x + 2)
        yr = min(yr[0], y - 1), max(yr[1], y + 2)
        zr = min(zr[0], z - 1), max(zr[1], z + 2)

    state = set()
    for x in range(*xr):
        for y in range(*yr):
            for z in range(*zr):
                active_neighbors = sum(1 for n in neighbors(x, y, z) if n in points)
                if active_neighbors == 3:
                    state.add((x, y, z))
                elif active_neighbors == 2:
                    p = (x, y, z)
                    if p in points:
                        state.add(p)
    return state


def part_one(model, cycles=6):
    for _ in range(cycles):
        model = tick(model)
    return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
    )

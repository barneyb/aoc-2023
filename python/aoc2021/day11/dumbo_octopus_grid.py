from util import aoc


def parse(input):
    os = []
    for line in input.splitlines():
        os.append([int(o) for o in line])
    return len(os[0]), len(os), os


def unparse(model):
    w, h, os = model
    sb = []
    for row in os:
        sb.extend(str(o) for o in row)
        sb.append("\n")
    return "".join(sb)


def tick(model):
    """I move the model forward one tick, returning a tuple containing the next
    model and the number of flashes that occurred during the tick.
    """

    def neighbors(x, y):
        return [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            # me!
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]

    def in_bounds(x, y):
        return 0 <= x < w and 0 <= y < h

    def energize(x, y):
        if (x, y) in flashed:
            return  # only flash once per tick!
        octopuses[y][x] += 1
        if octopuses[y][x] <= 9:
            return
        # fully energized; flash!
        flashed.add((x, y))
        octopuses[y][x] = 0
        for x, y in neighbors(x, y):
            if in_bounds(x, y):
                energize(x, y)

    w, h, curr = model
    octopuses = [list(row) for row in curr]
    flashed = set()
    for y, row in enumerate(octopuses):
        for x, _ in enumerate(row):
            energize(x, y)
    return (w, h, octopuses), len(flashed)


def part_one(model, *, steps=100):
    total_flashes = 0
    curr = model
    for _ in range(steps):
        curr, flashes = tick(curr)
        total_flashes += flashes
    return total_flashes


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
    )

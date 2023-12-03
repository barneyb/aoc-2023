from util import aoc
from util.linear_grid import LinearGrid, parse_chars


def parse(input):
    return parse_chars(input, int)


def tick(model):
    """I move the model forward one tick, returning a tuple containing the next
    model and the number of flashes that occurred during the tick.
    """

    def energize(i):
        if i in flashed:
            return  # only flash once per tick!
        octopuses[i] += 1
        if octopuses[i] <= 9:
            return
        # fully energized; flash!
        flashed.add(i)
        octopuses[i] = 0
        for p in grid.neighbors(grid.to_point(i)):
            if grid.in_bounds(p):
                energize(grid.to_i(p))

    w, h, curr = model
    grid = LinearGrid(w, h)
    octopuses = list(curr)
    flashed = set()
    for i in range(len(octopuses)):
        energize(i)
    return (w, h, octopuses), len(flashed)


def part_one(model, *, steps=100):
    total_flashes = 0
    for _ in range(steps):
        model, flashes = tick(model)
        total_flashes += flashes
    return total_flashes


def part_two(model):
    w, h, _ = model
    count = w * h
    step = 0
    while True:
        step += 1
        model, flashes = tick(model)
        if flashes == count:
            return step


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

from util import aoc


def parse(input):
    w = None
    os = []
    for line in input.splitlines():
        os.extend(int(o) for o in line)
        if w is None:
            w = len(os)
    return w, len(os) // w, os


def tick(model):
    """I move the model forward one tick, returning a tuple containing the next
    model and the number of flashes that occurred during the tick.
    """

    def to_i(x, y):
        return y * w + x

    def to_xy(i):
        return i % w, i // w

    def neighbors(p):
        x, y = p
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

    def in_bounds(p):
        x, y = p
        return 0 <= x < w and 0 <= y < h

    def energize(i):
        if i in flashed:
            return  # only flash once per tick!
        octopuses[i] += 1
        if octopuses[i] <= 9:
            return
        # fully energized; flash!
        flashed.add(i)
        octopuses[i] = 0
        for p in neighbors(to_xy(i)):
            if in_bounds(p):
                energize(to_i(*p))

    w, h, curr = model
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

from util import aoc


def parse(input):
    w = None
    os = []
    for line in input.splitlines():
        os.extend(int(o) for o in line)
        if w is None:
            w = len(os)
    return w, len(os) // w, os


def unparse(model):
    w, h, os = model
    sb = []
    end = w - 1
    for i, o in enumerate(os):
        assert 0 <= o < 10
        sb.append(str(o))
        if i % w == end:
            sb.append("\n")
    return "".join(sb)


def tick(model):
    """I move the model forward one tick, and return a tuple containing the next
    model and the number of flashes during the tick.
    """
    w, h, curr = model

    def to_i(x, y):
        return y * w + x

    def to_xy(i):
        return i % w, i // w

    def neighbors(i):
        x, y = to_xy(i)
        if x > 0:
            if y > 0:
                yield to_i(x - 1, y - 1)
            yield to_i(x - 1, y)
            if y < h - 1:
                yield to_i(x - 1, y + 1)
        if y > 0:
            yield to_i(x, y - 1)
        # it's me!
        if y < h - 1:
            yield to_i(x, y + 1)
        if x < w - 1:
            if y > 0:
                yield to_i(x + 1, y - 1)
            yield to_i(x + 1, y)
            if y < h - 1:
                yield to_i(x + 1, y + 1)

    def energize(i):
        if i in flashed:
            return
        octopuses[i] += 1
        if octopuses[i] > 9:
            flashed.add(i)
            octopuses[i] = 0
            for n in neighbors(i):
                energize(n)

    octopuses = list(curr)
    flashed = set()
    for i in range(len(octopuses)):
        energize(i)
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

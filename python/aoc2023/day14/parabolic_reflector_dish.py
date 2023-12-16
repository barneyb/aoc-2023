from util import aoc


def parse(input):
    rocks = {}
    lines = input.splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in "O#":
                rocks[(x, y)] = c
    return len(lines[0]), len(lines), rocks


def weight_on_north_support(model):
    _, h, rocks = model
    return sum(h - y for (_, y), r in rocks.items() if r == "O")


def part_one(model):
    w, h, curr = model
    rocks = {}
    for (x, y), r in curr.items():
        if r == "#":
            rocks[(x, y)] = r
            continue
        while y > 0 and (x, y - 1) not in rocks:
            y -= 1
        rocks[(x, y)] = r
    return weight_on_north_support((w, h, rocks))


_spin = [
    (lambda p: p[1], lambda p: (p[0], p[1] - 1)),
    (lambda p: p[0], lambda p: (p[0] - 1, p[1])),
    (lambda p: -p[1], lambda p: (p[0], p[1] + 1)),
    (lambda p: -p[0], lambda p: (p[0] + 1, p[1])),
]


def in_bounds(p, w, h):
    x, y = p
    return 0 <= x < w and 0 <= y < h


def spin_cycle(model):
    w, h, rocks = model
    for key, delta in _spin:
        curr = rocks
        rocks = {}
        for p in sorted(curr.keys(), key=key):
            r = curr[p]
            if r == "#":
                rocks[p] = r
                continue
            while True:
                candidate = delta(p)
                if in_bounds(candidate, w, h) and candidate not in rocks:
                    p = candidate
                else:
                    break
            rocks[p] = r
    return w, h, rocks


def spin_cycles(model, total_cycles):
    history = {}
    for i in range(total_cycles):
        s = frozenset(model[2])
        if s in history:
            cycle_len = i - history[s]
            full_cycles = (total_cycles - i) // cycle_len
            to_align = total_cycles - full_cycles * cycle_len - i
            return spin_cycles(model, to_align)
        history[s] = i
        model = spin_cycle(model)
    return model


def part_two(model):
    return weight_on_north_support(spin_cycles(model, 1_000_000_000))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

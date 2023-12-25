from collections import Counter, deque

from util import aoc


class Garden:
    def __init__(self, input):
        lines = input.splitlines()
        self.width = len(lines[0])
        self.height = len(lines)
        self.rocks = set()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "S":
                    self.start = (x, y)
                elif c == "#":
                    self.rocks.add((x, y))

    def neighbors(self, p):
        x, y = p
        return [
            p
            for p in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
            if p not in self.rocks
        ]

    def __str__(self):
        sb = []
        for y in range(self.height):
            for x in range(self.width):
                p = (x, y)
                sb.append("#" if p in self.rocks else "S" if p == self.start else ".")
            sb.append("\n")
        return "".join(sb)

    def __repr__(self):
        return "Garden('" + str(self) + "')"


def part_one(garden, steps=64):
    locs = set()
    locs.add(garden.start)
    for _ in range(steps):
        prev = locs
        locs = set()
        for p in prev:
            locs.update(garden.neighbors(p))
    return len(locs)


def part_two(garden, steps=26_501_365):
    locs = {garden.start: {(0, 0)}}
    saturation_count = None
    saturation = deque(maxlen=5)
    target = None
    other = None
    stable_gardens = {}  # step the garden reached stable target
    for step in range(steps):
        prev = locs
        locs = {}
        for p, gdns in prev.items():
            for lc in garden.neighbors(p):
                gs = gdns
                nx, ny = lc
                if nx < 0:
                    nx += garden.width
                    gs = [(x - 1, y) for x, y in gs]
                elif nx >= garden.width:
                    nx -= garden.width
                    gs = [(x + 1, y) for x, y in gs]
                elif ny < 0:
                    ny += garden.height
                    gs = [(x, y - 1) for x, y in gs]
                elif ny >= garden.height:
                    ny -= garden.height
                    gs = [(x, y + 1) for x, y in gs]
                lc = (nx, ny)
                if lc not in locs:
                    locs[lc] = set()
                locs[lc].update(
                    (g for g in gs if g not in stable_gardens) if other else gs
                )
        if not saturation_count:
            saturation.append(len(locs))
            if len(saturation) >= 4:
                sat = saturation[0]
                if all(st == sat for st in saturation):
                    saturation_count = sat
                    del saturation
        hist = Counter()
        for gs in locs.values():
            for g in gs:
                hist[g] += 1
        if saturation_count and (not target or not other):
            if target is None:
                target = hist[(0, 0)]
                stable_gardens[(0, 0)] = step
            else:
                other = hist[(0, 0)]
        for g, c in hist.items():
            if c == target:
                stable_gardens[g] = step

    total = 0
    for gs in locs.values():
        for g in gs:
            if not other or g not in stable_gardens:
                total += 1
    if other:
        for g in stable_gardens:
            total += other if (step - stable_gardens[g]) % 2 else target
    return total


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Garden,
        part_one,
        part_two,
    )

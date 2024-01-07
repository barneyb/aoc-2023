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
    locs = set()
    px, py = garden.start
    locs.add((px, py, 0, 0))
    for _ in range(steps):
        prev = locs
        locs = set()
        for px, py, gx, gy in prev:
            for nx, ny in garden.neighbors((px, py)):
                if nx < 0:
                    locs.add((nx + garden.width, ny, gx - 1, gy))
                elif nx >= garden.width:
                    locs.add((nx - garden.width, ny, gx + 1, gy))
                elif ny < 0:
                    locs.add((nx, ny + garden.height, gx, gy - 1))
                elif ny >= garden.height:
                    locs.add((nx, ny - garden.height, gx, gy + 1))
                else:
                    locs.add((nx, ny, gx, gy))
    return len(locs)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Garden,
        part_one,
        part_two,
    )

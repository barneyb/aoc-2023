import math
from heapq import heappop, heappush

from util import aoc


def parse(input):
    lines = input.splitlines()
    return len(lines[0]), len(lines), [[int(d) for d in l] for l in lines]


def part_one(model):
    def in_bounds(x, y):
        return 0 <= x < width and 0 <= y < height

    def move(pos, d):
        x, y = pos
        match d:
            case 0:
                return x, y - 1
            case 1:
                return x + 1, y
            case 2:
                return x, y + 1
            case 3:
                return x - 1, y

    def heat_loss(x, y):
        return layout[y][x]

    width, height, layout = model
    start = (0, 0)
    goal = (width - 1, height - 1)
    best = math.inf
    visited = set()
    pq = [(0, start, ())]
    while len(pq):
        hl, pos, path = heappop(pq)
        if (pos, path) in visited:
            continue
        if hl >= best:
            continue
        if pos == goal:
            best = hl
            continue
        visited.add((pos, path))
        reverse = (path[-1] + 2) % 4 if len(path) else None
        straight = None
        if len(path) == 3:
            a, b, c = path
            if a == b == c:
                straight = a
        for d in range(4):
            if d == reverse or d == straight:
                continue
            p = move(pos, d)
            if in_bounds(*p):
                np = path[-2:] + (d,)
                if (p, np) not in visited:
                    heappush(pq, (hl + heat_loss(*p), p, np))

    return best


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

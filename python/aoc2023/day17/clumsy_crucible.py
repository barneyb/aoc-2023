import math
from collections import defaultdict
from heapq import heappop, heappush

from util import aoc


def parse(input):
    lines = input.splitlines()
    return len(lines[0]), len(lines), [[int(d) for d in l] for l in lines]


def render(model, path):
    width, height, layout = model
    sb = []
    for y, line in enumerate(layout):
        for x, l in enumerate(line):
            if (x, y) in path:
                sb.append(path[(x, y)])
            else:
                sb.append(str(l))
        sb.append("   ")
        for x, l in enumerate(line):
            if (x, y) in path:
                sb.append(str(l))
            else:
                sb.append(".")
        sb.append("\n")
    return "".join(sb)


def arrow(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return "↑" if y1 > y2 else "←" if x1 > x2 else "↓" if y1 < y2 else "→"


def part_one(model):
    def in_bounds(x, y):
        return 0 <= x < width and 0 <= y < height

    def neighbors(p):
        x, y = p
        return [
            (a, b)
            for a, b in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
            if in_bounds(a, b)
        ]

    def heat_loss(p):
        x, y = p
        return layout[y][x]

    width, height, layout = model
    start = (0, 0)
    goal = (width - 1, height - 1)
    visited = set()
    loss_at = defaultdict(lambda: math.inf)
    loss_at[start] = 0  # heat loss starts as 0
    prev = {}
    pq = [(0, start)]
    while len(pq):
        hl, curr = heappop(pq)
        visited.add(curr)
        if hl >= loss_at[goal]:
            continue
        for n in neighbors(curr):
            if n not in visited:
                alt = hl + heat_loss(n)
                if alt < loss_at[n]:
                    loss_at[n] = alt
                    prev[n] = curr
                    heappush(pq, (alt, n))
    curr = goal
    path = {}
    while curr in prev:
        p = prev[curr]
        path[curr] = arrow(p, curr)
        curr = p
    print("\n" + render(model, path))
    return loss_at[goal]


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

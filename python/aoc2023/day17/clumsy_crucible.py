import math
from heapq import heappop, heappush

from util import aoc
from util.geom_2d import move


class Map:
    def __init__(self, input):
        lines = input.splitlines()
        self.width = len(lines[0])
        self.height = len(lines)
        self.grid = [[int(c) for c in l] for l in lines]
        self.goal = (self.width - 1, self.height - 1)

    def __contains__(self, p):
        x, y = p
        return 0 <= x < self.width and 0 <= y < self.height

    def __getitem__(self, p):
        x, y = p
        return self.grid[y][x]

    def heat_loss(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            ys = range(y1 + 1, y2 + 1) if y1 < y2 else range(y2, y1)
            return sum(self.grid[y][x1] for y in ys)
        line = self.grid[y1]
        if x1 < x2:
            return line[x2] if x2 == x1 + 1 else sum(line[x1 + 1 : x2 + 1])
        return line[x2] if x1 == x2 + 1 else sum(line[x2:x1])


def either_part(map: Map, allowed_moves):
    """Returns the minimal heat loss through the city, using allowed_moves to
    get an iterable of moves a given state can transition to.
    """
    best = math.inf
    visited = set()
    pq = [(0, (0, 0), ())]
    while len(pq):
        loss, pos, path = heappop(pq)
        v = (pos, path)
        if loss >= best or v in visited:
            continue
        if pos == map.goal:
            best = loss
            continue
        visited.add(v)
        for p, np in allowed_moves(pos, path):
            if (p, np) not in visited:
                heappush(pq, (loss + map.heat_loss(pos, p), p, np))

    return best


def part_one(map: Map):
    def allowed_moves(pos, path):
        if not len(path):
            return [(move(pos, d), (d,)) for d in (1, 2)]
        reverse = (path[-1] + 2) % 4
        straight = None
        if len(path) == 3:
            a, b, c = path
            if a == b == c:
                straight = a
        return [
            (m, path[-2:] + (d,))
            for m, d in [
                (move(pos, d), d) for d in range(4) if d != reverse and d != straight
            ]
            if m in map
        ]

    return either_part(map, allowed_moves)


def part_two(map: Map):
    def allowed_moves(pos, path):
        if not len(path):
            return [(move(pos, d, 4), (d,) * 4) for d in (1, 2)]
        heading = path[-1]
        steps = []
        if len(path) < 10 or any(d != heading for d in path):
            steps.append((heading, 1))
        if heading % 2 == 1:  # running east-west
            steps.append((0, 4))
            steps.append((2, 4))
        if heading % 2 == 0:  # running north-south
            steps.append((1, 4))
            steps.append((3, 4))
        return [
            (m, path[n - 10 :] + (d,) * n)
            for m, d, n in [(move(pos, d, n), d, n) for d, n in steps]
            if m in map
        ]

    return either_part(map, allowed_moves)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Map,
        part_one,
        part_two,
    )

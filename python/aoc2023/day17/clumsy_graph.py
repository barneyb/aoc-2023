import math
from heapq import heappop, heappush

from util import aoc


class NotEnoughRoom(RuntimeError):
    pass


class Graph:
    def __init__(self, input):
        lines = input.splitlines()
        height = len(lines)
        width = len(lines[0])
        self.start = 0
        self.goal = width * height - 1
        self.nodes = [
            (int(c), []) for y, line in enumerate(lines) for x, c in enumerate(line)
        ]

        def add_edges(i, j, d):
            ic, ia = self.nodes[i]
            jc, ja = self.nodes[j]
            ia.append((j, jc, d))
            ja.append((i, ic, (d + 2) % 4))
            pass

        for y in range(height):
            for x in range(width):
                i = y * width + x
                if y > 0:
                    add_edges(i, (y - 1) * width + x, 0)
                if x > 0:
                    add_edges(i, y * width + x - 1, 3)

    def edges(self, n):
        return self.nodes[n][1]


def either_part(G, allowed_moves):
    pq = [(0, G.start, ())]
    visited = set()
    best = math.inf
    while len(pq):
        loss, pos, path = heappop(pq)
        v = (pos, path)
        if loss >= best or v in visited:
            continue
        if pos == G.goal:
            best = loss
            continue
        visited.add(v)
        for n, l, np in allowed_moves(pos, path):
            if (n, np) not in visited:
                heappush(pq, (loss + l, n, np))
    return best


def part_one(G):
    def allowed_moves(pos, path):
        for n, l, d in G.edges(pos):
            if len(path) and (d + 2) % 4 == path[-1]:
                continue  # no reverse
            if len(path) == 3 and all(p == d for p in path):
                continue  # no four in a row
            yield n, l, path[-2:] + (d,)

    return either_part(G, allowed_moves)


def part_two(G):
    def extend(n, l, np):
        d = np[-1]
        while any(p != d for p in np[-4:]):
            found = False
            for a, b, c in G.edges(n):
                if d == c:
                    found = True
                    n = a
                    l += b
                    np = np[-9:] + (d,)
                    break
            if not found:
                raise NotEnoughRoom
        return n, l, np

    def allowed_moves(pos, path):
        for n, l, d in G.edges(pos):
            heading = path[-1] if len(path) else d
            if (d + 2) % 4 == heading:
                continue  # no reverse
            if n == G.goal:
                if d != heading or any(p != heading for p in path[-3:]):
                    continue
            if len(path) == 10 and d == heading:
                if all(p == heading for p in path):
                    continue  # no more than 10
            try:
                yield extend(n, l, path[-9:] + (d,))
            except NotEnoughRoom:
                pass

    return either_part(G, allowed_moves)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Graph,
        part_one,
        part_two,
    )

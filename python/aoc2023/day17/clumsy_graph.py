import math
from heapq import heappop, heappush

from util import aoc


class Graph:
    def __init__(self, input):
        lines = input.splitlines()
        height = len(lines)
        width = len(lines[0])
        self.start = 0
        self.goal = width * height - 1
        self.nodes = [None for _ in range(self.goal + 1)]
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                self.nodes[y * width + x] = (x, y, int(c), [])

        def add_edges(i, j, d):
            _, _, ic, ia = self.nodes[i]
            _, _, jc, ja = self.nodes[j]
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
        return self.nodes[n][3]


def either_part(G, path_len, accept):
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
        for n, l, d in G.edges(pos):
            if not accept(path, d, n):
                continue
            np = path[1 - path_len :] + (d,)
            if (n, np) not in visited:
                heappush(pq, (loss + l, n, np))
    return best


def part_one(G):
    def accept(path, d, n):
        if len(path) and (d + 2) % 4 == path[-1]:
            return False  # no reverse
        if len(path) == 3 and all(p == d for p in path):
            return False  # no four in a row
        return True

    return either_part(G, 3, accept)


def part_two(G):
    def accept(path, d, n):
        if not len(path):
            return True
        heading = path[-1]
        if (d + 2) % 4 == heading:
            return False  # no reverse
        if n == G.goal:
            return d == heading and all(p == heading for p in path[-3:])
        if len(path) < 4 or any(p != heading for p in path[-4:]):
            return d == heading  # at least four
        if len(path) == 10 and d == heading:
            return any(p != heading for p in path)  # no more than 10
        return True

    return either_part(G, 10, accept)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Graph,
        part_one,
        part_two,
    )

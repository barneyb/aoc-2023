import math
from heapq import heappop, heappush

from util import aoc


class NotEnoughRoom(RuntimeError):
    pass


class Graph:
    def __init__(self, input):
        def add_edges(i, j, d):
            ic, ia = pairs[i]
            jc, ja = pairs[j]
            ia.append((j, jc, d))
            ja.append((i, ic, (d + 2) % 4))

        lines = input.splitlines()
        height = len(lines)
        width = len(lines[0])
        pairs = [(int(c), []) for line in lines for c in line]
        for y in range(height):
            for x in range(width):
                i = y * width + x
                if y > 0:
                    add_edges(i, i - width, 0)
                if x > 0:
                    add_edges(i, i - 1, 3)

        self.start = 0
        self.goal = width * height - 1
        self.nodes = [es for _, es in pairs]
        self[self.goal].clear()  # no leaving the goal!

    def __getitem__(self, n):
        return self.nodes[n]


def either_part(graph, allowed_moves):
    pq = [(0, graph.start, ())]
    visited = set()
    best = math.inf
    while len(pq):
        loss, pos, path = heappop(pq)
        v = (pos, path)
        if loss >= best or v in visited:
            continue
        if pos == graph.goal:
            best = loss
            continue
        visited.add(v)
        for n, l, np in allowed_moves(pos, path):
            if (n, np) not in visited:
                heappush(pq, (loss + l, n, np))
    return best


def part_one(graph):
    def allowed_moves(pos, path):
        for n, l, d in graph[pos]:
            if len(path) and (d + 2) % 4 == path[-1]:
                continue  # no reverse
            if len(path) == 3 and all(p == d for p in path):
                continue  # no four in a row
            yield n, l, path[-2:] + (d,)

    return either_part(graph, allowed_moves)


def part_two(graph):
    def extend(n, l, path, d):
        for _ in range(1, 4):
            for a, b, c in graph[n]:
                if d == c:
                    n = a
                    l += b
                    break
            else:
                return
        yield n, l, path[-6:] + (d,) * 4

    def allowed_moves(pos, path):
        for n, l, d in graph[pos]:
            heading = d
            if len(path):
                heading = path[-1]
                if (d + 2) % 4 == heading:
                    continue  # no reverse
            turning = d != heading
            if n == graph.goal:
                if turning or any(p != heading for p in path[-3:]):
                    continue
            if len(path) == 10 and not turning:
                if all(p == heading for p in path):
                    continue  # no more than 10
            if turning:  # or any(p != d for p in path[-4:]):
                yield from extend(n, l, path, d)
            else:
                yield n, l, path[-9:] + (d,)

    return either_part(graph, allowed_moves)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Graph,
        part_one,
        part_two,
    )

from collections import Counter, deque

from util import aoc


class Trails:
    def __init__(self, input):
        def add_edge(u, v):
            if v in nodes:
                _, na = nodes[u]
                _, oa = nodes[v]
                oa.append((u, 1))
                na.append((v, 1))

        lines = input.splitlines()
        width = len(lines[0])
        nodes = {}
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    continue
                n = y * width + x
                nodes[n] = (c, [])
                add_edge(n, n - width)
                add_edge(n, n - 1)
        self.nodes = nodes
        self.width = width
        self.height = len(lines)
        self.start = min(nodes)
        self.goal = max(nodes)

    def to_coords(self, n):
        return n % self.width, n // self.height

    def __getitem__(self, n):
        return self.nodes[n][1]

    def __str__(self, highlight=None):
        sb = []
        for y in range(self.height):
            for x in range(self.width):
                n = y * self.width + x
                if n not in self.nodes:
                    sb.append("#")
                    continue
                if highlight and n in highlight:
                    sb.append("O")
                else:
                    sb.append(self.nodes[n][0])
            sb.append("\n")
        return "".join(sb)


class SlipperyTrails(Trails):
    def __getitem__(self, n):
        c, adj = self.nodes[n]
        if c == ".":
            return adj
        elif c == "^":
            adj = [n - self.width]
        elif c == ">":
            adj = [n + 1]
        elif c == "v":
            adj = [n + self.width]
        elif c == "<":
            adj = [n - 1]
        adj = [(n, 1) for n in adj]
        self.nodes[n] = (".", adj)
        return adj


def longest_hikes(trails, start, goals):
    queue = deque()
    queue.append((start, {}, 0))
    longest = Counter()
    while queue:
        p, visited, dist = queue.pop()
        if dist > longest[p]:
            longest[p] = dist
        if p in goals and dist > 0:
            continue
        visited = set(visited)
        visited.add(p)
        queue.extend((n, visited, dist + d) for n, d in trails[p] if n not in visited)
    return {g: longest[g] for g in goals if g in longest and g != start}


def find_forks(trails):
    forks = []
    visited = set()
    queue = deque()
    queue.append(trails.start)
    while queue:
        p = queue.pop()
        if p in visited:
            continue
        visited.add(p)
        ns = trails[p]
        if len(ns) > 2:
            forks.append(p)
        queue.extend(n for n, _ in ns if n not in visited)
    return forks


def either_part(trails):
    forks = set(find_forks(trails))
    forks.add(trails.start)
    forks.add(trails.goal)
    compressed = {}
    for f in forks:
        compressed[f] = [p for p in longest_hikes(trails, f, forks).items()]
    hikes = longest_hikes(compressed, trails.start, {trails.goal})
    return hikes[trails.goal]


def part_one(input):
    return either_part(SlipperyTrails(input))


def part_two(input):
    return either_part(Trails(input))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        None,
        part_one,
        part_two,
    )

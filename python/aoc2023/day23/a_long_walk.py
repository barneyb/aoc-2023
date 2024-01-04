import math
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


def multi_bfs(trails, start, goals):
    queue = deque()
    queue.append((start, 0))
    bests = Counter()
    visited = set()
    while queue:
        p, dist = queue.popleft()
        if p in visited:
            continue
        visited.add(p)
        if dist > bests[p]:
            bests[p] = dist
        if p in goals and dist > 0:
            continue
        queue.extend((n, dist + d) for n, d in trails[p] if n not in visited)
    return {g: bests[g] for g in goals if g in bests and g != start}


def dfs(trails, u, goal, visited):
    if u == goal:
        return 0
    visited.add(u)
    best = -math.inf
    for v, w in trails[u]:
        if v not in visited:
            best = max(best, w + dfs(trails, v, goal, visited))
    visited.remove(u)
    return best


def either_part(trails):
    forks = set(find_forks(trails))
    forks.add(trails.start)
    forks.add(trails.goal)
    compressed = {}
    for f in forks:
        compressed[f] = [p for p in multi_bfs(trails, f, forks).items()]
    return dfs(compressed, trails.start, trails.goal, set())


def graph_viz(trails, start, goal):
    edges = {}
    print("graph {")
    print(f"  {'{'} rank=source; {start} {'}'}")
    print(f"  {'{'} rank=sink; {goal} {'}'}")
    print(f"  {start} [color=red, shape=box]")
    print(f"  {goal} [color=red, shape=box]")
    for u in trails:
        for v, d in trails[u]:
            e = (u, v) if u < v else (v, u)
            if e not in edges or edges[e] != d:
                edges[e] = d
                print(f"  {u} -- {v} [label={d}]")
    print("}")


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

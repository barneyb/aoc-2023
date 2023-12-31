import random
from collections import defaultdict

from util import aoc


class Graph:
    def __init__(self, edges):
        self.nodes = defaultdict(lambda: (1, []))
        for u, v in edges:
            self.add_edge(u, v)

    def add_edge(self, u, v):
        self.nodes[u][1].append(v)
        self.nodes[v][1].append(u)

    def remove_edge(self, u, v):
        self.nodes[u][1].remove(v)
        self.nodes[v][1].remove(u)

    def contract(self, u, v):
        uw, uadj = self.nodes[u]
        vw, vadj = self.nodes[v]
        uv = len(self.nodes)  # safe: contraction ensures a decrease in size
        self.nodes[uv] = uw + vw, []
        for w in uadj:
            if w != v:
                self.add_edge(w, uv)
            self.nodes[w][1].remove(u)
        for w in vadj:
            if w != u:
                self.add_edge(w, uv)
            self.nodes[w][1].remove(v)
        del self.nodes[u]
        del self.nodes[v]

    def degree(self, u):
        return len(self.nodes[u][1])

    def weight(self, u):
        return self.nodes[u][0]

    def __iter__(self):
        return iter(self.nodes)

    def __getitem__(self, n):
        return self.nodes[n][1]

    def __len__(self):
        return len(self.nodes)


def parse(input):
    edges = []
    for line in input.splitlines():
        a, rest = line.split(":")
        for b in rest.strip().split(" "):
            edges.append((a, b))
    return edges


def part_one(edges):
    # The problem says what the minimum cut's size is (3), so run Karger's until
    # we get that result. Whatever partition the cut makes is the answer.
    rounds = 0
    while True:
        rounds += 1
        graph = Graph(edges)
        while len(graph) > 2:
            # todo: this is neither performant nor random. But it's sufficient!
            ns = list(graph)
            u = ns[random.randint(0, len(ns) - 1)]
            es = graph[u]
            v = es[random.randint(0, len(es) - 1)]
            graph.contract(u, v)
        if all(len(graph[u]) == 3 for u in graph):
            a, b = [graph.weight(u) for u in graph]
            return a * b, rounds


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
    )

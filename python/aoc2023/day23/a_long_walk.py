from collections import deque

from util import aoc


class Paths:
    def __init__(self, input):
        def add_edge(n, o):
            if o in nodes:
                _, na = nodes[n]
                _, oa = nodes[o]
                oa.append(n)
                na.append(o)

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
        self.nodes[n] = (".", adj)
        return adj

    def __str__(self):
        sb = []
        for y in range(self.height):
            for x in range(self.width):
                n = y * self.width + x
                if n not in self.nodes:
                    sb.append("#")
                    continue
                sb.append(self.nodes[n][0])
            sb.append("\n")
        return "".join(sb)


def part_one(paths):
    queue = deque()
    queue.append((paths.start, []))
    longest = -1
    while queue:
        p, path = queue.popleft()
        if p == paths.goal:
            longest = max(longest, len(path))
            continue
        path = list(path)
        path.append(p)
        for n in paths[p]:
            if n not in path:
                queue.append((n, path))
        pass
    return longest


# def part_two(path):
#     return None


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Paths,
        part_one,
        # part_two,
    )

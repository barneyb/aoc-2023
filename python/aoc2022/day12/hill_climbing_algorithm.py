from collections import deque

from util import aoc


class Map:
    def __init__(self, input):
        super().__init__()
        lines = input.splitlines()
        self.width = len(lines[0])
        self.height = len(lines)
        self.start = None
        self.end = None
        for y, row in enumerate(lines):
            x = row.find("S")
            if x >= 0:
                lines[y] = row = row.replace("S", "a")
                self.start = (x, y)
                if self.end is not None:
                    break
            x = row.find("E")
            if x >= 0:
                lines[y] = row.replace("E", "z")
                self.end = (x, y)
                if self.start is not None:
                    break
        self.map = [[ord(c) for c in row] for row in lines]

    def __str__(self):
        def to_char(p):
            c = "S" if p == self.start else "E" if p == self.end else chr(self[p])
            x, y = p
            return "\n" + c if x == 0 and y > 0 else c

        return "".join(to_char(p) for p in self)

    def __contains__(self, p):
        x, y = p
        return 0 <= x < self.width and 0 <= y < self.height

    def __getitem__(self, p):
        x, y = p
        return self.map[y][x]

    def __iter__(self):
        for y in range(self.height):
            for x in range(self.width):
                yield x, y

    def neighbors(self, p):
        x, y = p
        max_e = self[p] + 1
        return filter(
            lambda p: p in self and self[p] <= max_e,
            [
                (x, y - 1),
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
            ],
        )


def part_one(map, start=None):
    visited = set()
    queue = deque([(start if start else map.start, 0)])
    while len(queue) != 0:
        curr, steps = queue.popleft()
        if curr not in visited:
            visited.add(curr)
            steps += 1
            for n in map.neighbors(curr):
                if n == map.end:
                    return steps
                queue.append((n, steps))


def part_two(map):
    base_e = ord("a")
    return min(
        part_one(map, p)
        for p in map
        if map[p] == base_e and any(map[n] != base_e for n in map.neighbors(p))
    )


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Map,
        part_one,
        part_two,
    )

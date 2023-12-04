from collections import deque

from util import aoc

NO_PATH = 999_999_999


def parse(input):
    map = input.splitlines()
    dims = (len(map[0]), len(map))
    start = None
    end = None
    for y, row in enumerate(map):
        x = row.find("S")
        if x >= 0:
            map[y] = row = row.replace("S", "a")
            start = (x, y)
            if end is not None:
                break
        x = row.find("E")
        if x >= 0:
            map[y] = row.replace("E", "z")
            end = (x, y)
            if start is not None:
                break
    return dims, start, end, map


def part_one(model):
    (w, h), start, end, map = model

    def elevation(p):
        x, y = p
        return ord(map[y][x])

    def in_bounds(p):
        x, y = p
        return 0 <= x < w and 0 <= y < h

    def neighbors(p):
        x, y = p
        max_e = elevation(p) + 1
        return filter(
            lambda p: in_bounds(p) and elevation(p) <= max_e,
            [
                (x, y - 1),
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
            ],
        )

    visited = set()
    queue = deque()
    queue.append((start, 0))
    while len(queue) != 0:
        curr, steps = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        steps += 1
        for n in neighbors(curr):
            if n == end:
                return steps
            queue.append((n, steps))
    return NO_PATH


def part_two(model):
    dims, _, end, map = model
    best = NO_PATH
    for y, row in enumerate(map):
        x = -1
        while True:
            x = row.find("a", x + 1)
            if x < 0:
                break
            steps = part_one((dims, (x, y), end, map))
            if steps < best:
                best = steps
    return best


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

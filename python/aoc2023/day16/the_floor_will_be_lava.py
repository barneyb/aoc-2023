from collections import deque
from enum import Enum

from util import aoc


class Dir(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def trbl(self, p):
        x, y = p
        match self:
            case Dir.NORTH:
                return (x + 1, y), Dir.EAST
            case Dir.EAST:
                return (x, y - 1), Dir.NORTH
            case Dir.SOUTH:
                return (x - 1, y), Dir.WEST
            case Dir.WEST:
                return (x, y + 1), Dir.SOUTH

    def tlbr(self, p):
        x, y = p
        match self:
            case Dir.NORTH:
                return (x - 1, y), Dir.WEST
            case Dir.EAST:
                return (x, y + 1), Dir.SOUTH
            case Dir.SOUTH:
                return (x + 1, y), Dir.EAST
            case Dir.WEST:
                return (x, y - 1), Dir.NORTH

    def cont(self, p):
        x, y = p
        match self:
            case Dir.NORTH:
                return (x, y - 1), self
            case Dir.EAST:
                return (x + 1, y), self
            case Dir.SOUTH:
                return (x, y + 1), self
            case Dir.WEST:
                return (x - 1, y), self


def parse(input):
    layout = {}
    lines = input.splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in "\\/-|":
                layout[(x, y)] = c
    return len(lines[0]), len(lines), layout


def part_one(model):
    def in_bounds(p):
        x, y = p
        return 0 <= x < width and 0 <= y < height

    width, height, layout = model
    visited = set()
    energized = set()
    queue = deque()
    queue.append(((0, 0), Dir.EAST))
    while len(queue):
        curr = queue.pop()
        p, heading = curr
        if not in_bounds(p):
            continue
        if curr in visited:
            continue
        visited.add(curr)
        energized.add(p)
        if p not in layout:
            queue.append(heading.cont(p))
            continue
        match layout[p]:
            case "/":
                queue.append(heading.trbl(p))
            case "\\":
                queue.append(heading.tlbr(p))
            case "|" if heading in [Dir.NORTH, Dir.SOUTH]:
                queue.append(heading.cont(p))
            case "|":  # split
                x, y = p
                queue.append(((x, y - 1), Dir.NORTH))
                queue.append(((x, y + 1), Dir.SOUTH))
            case "-" if heading in [Dir.EAST, Dir.WEST]:
                queue.append(heading.cont(p))
            case "-":  # split
                x, y = p
                queue.append(((x + 1, y), Dir.EAST))
                queue.append(((x - 1, y), Dir.WEST))
    return len(energized)


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

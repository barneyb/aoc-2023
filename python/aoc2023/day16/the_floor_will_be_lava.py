from collections import Counter, deque
from enum import Enum

from util import aoc


class Dir(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def parse(input):
    layout = {}
    lines = input.splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in "\\/-|":
                layout[(x, y)] = c
    return len(lines[0]), len(lines), layout


def energized(model, beam):
    def thru():
        match heading:
            case Dir.NORTH:
                return (x, y - 1), heading
            case Dir.EAST:
                return (x + 1, y), heading
            case Dir.SOUTH:
                return (x, y + 1), heading
            case Dir.WEST:
                return (x - 1, y), heading

    width, height, layout = model
    visited, energized = set(), Counter()
    queue = deque([beam])
    while len(queue):
        curr = queue.pop()
        p, heading = curr
        x, y = p
        if not (0 <= x < width and 0 <= y < height):
            continue
        energized[p] += 1
        if curr in visited:
            continue
        visited.add(curr)
        if p not in layout:  # an open square
            queue.append(thru())
            continue
        match layout[p]:
            case "/":
                match heading:
                    case Dir.NORTH:
                        queue.append(((x + 1, y), Dir.EAST))
                    case Dir.EAST:
                        queue.append(((x, y - 1), Dir.NORTH))
                    case Dir.SOUTH:
                        queue.append(((x - 1, y), Dir.WEST))
                    case Dir.WEST:
                        queue.append(((x, y + 1), Dir.SOUTH))
            case "\\":
                match heading:
                    case Dir.NORTH:
                        queue.append(((x - 1, y), Dir.WEST))
                    case Dir.EAST:
                        queue.append(((x, y + 1), Dir.SOUTH))
                    case Dir.SOUTH:
                        queue.append(((x + 1, y), Dir.EAST))
                    case Dir.WEST:
                        queue.append(((x, y - 1), Dir.NORTH))
            case "|" if heading in [Dir.NORTH, Dir.SOUTH]:  # through
                queue.append(thru())
            case "|":  # split
                queue.append(((x, y - 1), Dir.NORTH))
                queue.append(((x, y + 1), Dir.SOUTH))
            case "-" if heading in [Dir.EAST, Dir.WEST]:  # through
                queue.append(thru())
            case "-":  # split
                queue.append(((x + 1, y), Dir.EAST))
                queue.append(((x - 1, y), Dir.WEST))
    return energized


def part_one(model):
    return len(energized(model, ((0, 0), Dir.EAST)))


def every_source(model):
    width, height, _ = model
    for x in range(width):
        yield energized(model, ((x, 0), Dir.SOUTH))
        yield energized(model, ((x, height - 1), Dir.NORTH))
    for y in range(height):
        yield energized(model, ((0, y), Dir.EAST))
        yield energized(model, ((width - 1, y), Dir.WEST))


def part_two(model):
    return max(len(es) for es in every_source(model))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

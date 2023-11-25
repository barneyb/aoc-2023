from util import aoc


def parse(input):
    return [(s[0], int(s[1:])) for s in input.split(", ")]


def part_one(path):
    x, y = 0, 0
    for x, y in walk(path):
        pass
    return abs(x) + abs(y)


def walk(path):
    """Generator for all points along the path, which must be a sequence of
    tuples. Each tuple's first item is either 'R' or 'L', indicating which way
    to turn, and the second is how many steps to take after turning. The first
    point at the origin is not yielded (you're already there).
    """
    h, x, y = 0, 0, 0
    for d, n in path:
        h = h + 1 if d == 'R' else h - 1
        h %= 4
        for _ in range(n):
            match h:
                case 0:
                    y -= 1
                case 1:
                    x += 1
                case 2:
                    y += 1
                case 3:
                    x -= 1
            yield x, y


def part_two(path):
    points = set()
    for p in walk(path):
        if p in points:
            x, y = p
            return abs(x) + abs(y)
        points.add(p)


if __name__ == "__main__":
    aoc.solve(__file__,
              parse,
              part_one,
              part_two)

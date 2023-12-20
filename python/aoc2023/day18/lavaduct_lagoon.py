from collections import deque

from util import aoc


def parse_dir(c):
    match c:
        case "U" | "3":
            return 0
        case "R" | "0":
            return 1
        case "D" | "1":
            return 2
        case "L" | "2":
            return 3


def parse(input):
    return [
        (parse_dir(d), int(n), c[1:-1])
        for d, n, c in [l.split() for l in input.splitlines()]
    ]


def move(p, d, n=1):
    x, y = p
    match d:
        case 0:
            return x, y - n
        case 1:
            return x + n, y
        case 2:
            return x, y + n
        case 3:
            return x - n, y


def get_bounds(plan):
    x, y = 0, 0
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    corners = []
    prev_dirs = deque([plan[-1][0]], maxlen=2)
    for d, n in plan:
        if len(prev_dirs) == 2 and prev_dirs[0] != d:  # a 180
            pd = prev_dirs[1]
            if (pd + 1) % 4 == d:  # right
                x, y = move((x, y), pd, 1)
            else:  # left
                x, y = move((x, y), pd, -1)
        prev_dirs.append(d)
        corners.append((x, y))
        x, y = move((x, y), d, n)
        x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, x), max(y2, y)
    return (x1, y1), (x2, y2), corners


def get_rules(corners):
    (x1, _), (x2, _) = corners[0:2]
    if x1 == x2:  # rotate so horiz first
        first, *corners = corners
        corners.append(first)
    rules = []
    for i in range(0, len(corners), 2):
        a, b = corners[i : i + 2]
        (x1, y), (x2, _) = a, b
        rules.append((y, x1, x2))
    return rules


def part_one(model):
    plan = [(d, n) for d, n, _ in model]
    _, _, corners = get_bounds(plan)
    return get_rules(corners)


def parse_color(c):
    dist = int(c[1:-1], 16)
    return parse_dir(c[-1]), dist


def reparse(model):
    return [parse_color(c) for _, _, c in model]


def part_two(model):
    pass


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

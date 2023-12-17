import math
from heapq import heappop, heappush

from util import aoc


def parse(input):
    lines = input.splitlines()
    return len(lines[0]), len(lines), [[int(d) for d in l] for l in lines]


def move(pos, d, n=1):
    x, y = pos
    match d:
        case 0:
            return x, y - n
        case 1:
            return x + n, y
        case 2:
            return x, y + n
        case 3:
            return x - n, y


def either_part(model, allowed_moves):
    """Returns the minimal heat loss through the city, using allowed_moves to
    get an iterable of moves a given state can transition to.
    """

    def heat_loss(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            xs = range(x1, x1 + 1)
            ys = range(y1 + 1, y2 + 1) if y1 < y2 else range(y2, y1)
        else:
            xs = range(x1 + 1, x2 + 1) if x1 < x2 else range(x2, x1)
            ys = range(y1, y1 + 1)
        return sum(layout[y][x] for x in xs for y in ys)

    width, height, layout = model
    start = (0, 0)
    goal = (width - 1, height - 1)
    best = math.inf
    visited = set()
    pq = [(0, start, ())]
    while len(pq):
        hl, pos, path = heappop(pq)
        if hl >= best:
            continue
        if pos == goal:
            best = hl
            continue
        if (pos, path) in visited:
            continue
        visited.add((pos, path))
        for p, np in allowed_moves(pos, path, goal):
            if (p, np) not in visited:
                heappush(pq, (hl + heat_loss(pos, p), p, np))

    return best


def part_one(model):
    def allowed_moves(pos, path, goal):
        if not len(path):
            return [(move(pos, d), (d,)) for d in (1, 2)]
        reverse = (path[-1] + 2) % 4
        straight = None
        if len(path) == 3:
            a, b, c = path
            if a == b == c:
                straight = a
        steps = []
        x, y = pos
        w, h = goal
        if y > 0:
            steps.append(0)
        if x < w:
            steps.append(1)
        if y < h:
            steps.append(2)
        if x > 0:
            steps.append(3)
        return [
            (move(pos, d), path[-2:] + (d,))
            for d in steps
            if d != reverse and d != straight
        ]

    return either_part(model, allowed_moves)


def part_two(model):
    def allowed_moves(pos, path, goal):
        if not len(path):
            return [(move(pos, d, 4), (d, d, d, d)) for d in (1, 2)]
        run_len = 0
        of = path[-1]
        for d in reversed(path):
            if d != of:
                break
            run_len += 1
        steps = []
        x, y = pos
        w, h = goal
        if of % 2 == 1:  # running east-west
            if y > 3:
                steps.append((0, 4))
            if y < h - 3:
                steps.append((2, 4))
        if of % 2 == 0:  # running north-south
            if x < w - 3:
                steps.append((1, 4))
            if x > 3:
                steps.append((3, 4))
        if run_len < 10:  # can keep going
            if of == 0 and y > 0:
                steps.append((0, 1))
            if of == 1 and x < w:
                steps.append((1, 1))
            if of == 2 and y < h:
                steps.append((2, 1))
            if of == 3 and x > 0:
                steps.append((3, 1))
        return [(move(pos, d, n), path[n - 10 :] + (d,) * n) for d, n in steps]

    return either_part(model, allowed_moves)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

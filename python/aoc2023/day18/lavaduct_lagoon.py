from util import aoc


def parse_dir(c):
    match c:
        case "U":
            return 0
        case "R":
            return 1
        case "D":
            return 2
        case "L":
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


def cut_trench(plan):
    curr = (0, 0)
    trench = {curr: "#FF8000"}
    for d, n, c in plan:
        for _ in range(n):
            curr = move(curr, d)
            trench[curr] = c
    return trench


def bounds(trench):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    for x, y in trench:
        x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, x), max(y2, y)
    return (x1, y1), (x2, y2)


def find_point_inside(lo, hi, trench):
    y = (lo[1] + hi[1]) // 2
    inside = False
    x = lo[0]
    while x <= hi[0]:
        if not inside and (x, y) in trench:
            inside = True
        if inside and (x, y) not in trench:
            break
        x += 1
    return x, y


def dig_out_lagoon(trench, start):
    def enqueue(p):
        if p not in lagoon and p not in trench:
            queue.append(p)

    lagoon = set()
    queue = [start]
    while len(queue):
        p = queue.pop()
        if p in lagoon:
            continue
        lagoon.add(p)
        x, y = p
        enqueue((x, y - 1))
        enqueue((x + 1, y))
        enqueue((x, y + 1))
        enqueue((x - 1, y))
    return lagoon


def part_one(plan):
    trench = cut_trench(plan)
    lo, hi = bounds(trench)
    p = find_point_inside(lo, hi, trench)
    lagoon = dig_out_lagoon(trench, p)
    return len(trench) + len(lagoon)


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

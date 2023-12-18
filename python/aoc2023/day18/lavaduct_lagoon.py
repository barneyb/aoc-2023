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
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    for x, y in trench:
        x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, x), max(y2, y)
    return (x1, y1), (x2, y2), trench


def part_one(plan):
    lo, hi, trench = cut_trench(plan)
    print(f"{lo} -> {hi}")
    return len(trench)


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

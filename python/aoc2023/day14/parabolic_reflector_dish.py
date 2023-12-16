from util import aoc


def parse(input):
    rocks = {}
    lines = input.splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in "O#":
                rocks[(x, y)] = c
    return len(lines[0]), len(lines), rocks


def unparse(model):
    w, h, rocks = model
    sb = []
    for y in range(h):
        for x in range(w):
            p = (x, y)
            sb.append(rocks[p] if p in rocks else ".")
        sb.append("\n")
    return "".join(sb)


def part_one(model):
    w, h, curr = model
    rocks = {}
    for (x, y), r in curr.items():
        if r == "#":
            rocks[(x, y)] = r
            continue
        while y > 0 and (x, y - 1) not in rocks:
            y -= 1
        rocks[(x, y)] = r
    return sum(h - y for (_, y), r in rocks.items() if r == "O")


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

from collections import defaultdict

from util import aoc


def parse_brick(line):
    pts = line.split("~")
    a, b = [[int(d) for d in pt.split(",")] for pt in pts]
    if b < a:
        a, b = b, a
    return tuple((a, b + 1) for a, b in zip(a, b))


def parse(input):
    bricks = [parse_brick(l) for l in input.splitlines()]
    bricks.sort(key=lambda b: b[2])  # by lowest z
    return bricks


def draw(lbl, bricks):
    points = {}
    for i, ((x1, x2), (z1, z2)) in enumerate(bricks):
        for z in range(z1, z2):
            for x in range(x1, x2):
                p = (x, z)
                points[p] = "?" if p in points else chr(ord("A") + i)
    minx = min(x for x, _ in points)
    maxx = max(x for x, _ in points)
    maxz = max(z for _, z in points)
    midz = (maxz + 1) // 2
    print(f"\n {lbl}")
    print("".join(str(x) for x in range(minx, maxx + 1)))
    for z in range(maxz, 0, -1):
        line = ""
        for x in range(minx, maxx + 1):
            p = (x, z)
            line += points[p] if p in points else "."
        suffix = f"{z} z" if z == midz else str(z)
        print(f"{line} {suffix}")
    print(f"{'-' * (maxx-minx + 1)} 0")


def drop_bricks(bricks):
    heights = defaultdict(lambda: (0, -1))
    result = []
    for i, ((x1, x2), (y1, y2), (z1, z2)) in enumerate(bricks):
        floor = -1
        supported_by = []
        for x in range(x1, x2):
            for y in range(y1, y2):
                f, b = heights[(x, y)]
                if floor < f:
                    floor = f
                    supported_by = [b]
                elif floor == f:
                    supported_by.append(b)
        fall = z1 - floor - 1
        z1, z2 = z1 - fall, z2 - fall
        for x in range(x1, x2):
            for y in range(y1, y2):
                heights[(x, y)] = (z2 - 1, i)
        result.append(((x1, x2), (y1, y2), (z1, z2), set(supported_by)))
    return result


def part_one(bricks):
    bricks = drop_bricks(bricks)
    supports = {}
    for i, (_, _, _, supp_by) in enumerate(bricks):
        supports[i] = set()
        for b in supp_by:
            if b >= 0:
                supports[b].add(i)
    supported_by = defaultdict(lambda: set())
    for s, bs in supports.items():
        # noinspection PyStatementEffect
        supported_by[s]
        for b in bs:
            supported_by[b].add(s)
    can_disintegrate = []
    for i in range(len(bricks)):
        if all(len(supported_by[b]) > 1 for b in supports[i]):
            can_disintegrate.append(i)
    return len(can_disintegrate)


# def part_two(model):
#     return None


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

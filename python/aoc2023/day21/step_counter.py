from collections import defaultdict

from util import aoc


def parse(input):
    def edge(u, v):
        graph[u].append(v)
        graph[v].append(u)

    start = None
    lines = input.splitlines()
    width = len(lines[0])
    graph = [None] * (width * width)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                continue
            n = y * width + x
            graph[n] = []
            if c == "S":
                start = n
            left = n - 1
            if graph[left] is not None:
                edge(left, n)
            up = n - width
            if graph[up] is not None:
                edge(up, n)
    return start, graph, width


def part_one(model, steps=64):
    start, graph, width = model
    reached = {start}
    for _ in range(steps):
        reached = step(graph, reached)
    return len(reached)


def step(graph, reached):
    prev = reached
    reached = set()
    for n in prev:
        reached.update(graph[n])
    return reached


def get_edges(width):
    half = width // 2
    center = half * width + half
    north = half
    east = center + half
    south = half + width * (width - 1)
    west = center - half
    return north, east, south, west


def get_corners(width):
    nw = 0
    ne = width - 1
    sw = width * (width - 1)
    se = width * width - 1
    return nw, ne, se, sw


def part_two(model, steps=26_501_365):
    start, graph, width = model
    half = width // 2
    # assert (steps - half) % width == 0
    full_rounds = steps // width
    # after the initial half round and N full rounds:
    # 1 center tile, at 1.5 rounds
    # N-1 each cardinal tile, at 2 rounds
    # 1 each cardinal tile, at 1 round
    # triangle(N-2) each quadrant tile, at 2 rounds
    # N-1 each quadrant tile, at 1.5 rounds
    # N each quadrant tile, at .5 rounds

    # reached after 65 steps
    north, east, south, west = get_edges(width)
    # reached after 130 steps
    nw, ne, se, sw = get_corners(width)
    reached = {start}
    firsts = defaultdict(lambda: None)
    for s in range(width * 2):
        for n in [start, north, east, south, west, nw, ne, se, sw]:
            if n not in firsts and n in reached:
                # noinspection PyTypeChecker
                firsts[n] = s
        reached = step(graph, reached)
    for n in [north, east, south, west, nw, ne, se, sw]:
        print(f"reached {n} in {firsts[n]}")


def draw(model, reached, tl, br):
    start, graph, width = model
    x1, y1 = tl
    x2, y2 = br
    sb = []
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            n = y * width + x
            if x < 0 or x >= width:
                sb.append("-")
            elif y < 0 or y >= width:
                sb.append("|")
            elif n in reached:
                sb.append("O")
            elif n == start:
                sb.append("S")
            elif graph[n] is None:
                sb.append("#")
            else:
                sb.append(".")
        sb.append("\n")
    print("".join(sb))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

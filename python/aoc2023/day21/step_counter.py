import functools
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
            if x > 0:
                left = n - 1
                if graph[left] is not None:
                    edge(left, n)
            if y > 0:
                up = n - width
                if graph[up] is not None:
                    edge(up, n)
    return start, graph, width


def part_one(model, to_take=64):
    start, graph, width = model
    reached = {start}
    for _ in range(to_take):
        reached = take_step(graph, reached)
    return len(reached)


def part_two_simulate(model, to_take):
    gardens = simulate(model, to_take)
    print(to_string(model, gardens[0, 0]))
    # for g in sorted(gardens):
    #     print(f"{g}: {len(gardens[g])}")
    return sum(len(plots) for plots in gardens.values())


def simulate(model, to_take):
    start, graph, width = model
    gardens = {(0, 0): {start}}
    for _ in range(to_take):
        prev_gardens = gardens
        gardens = defaultdict(set)
        for (x, y), prev in prev_gardens.items():
            # step between gardens
            for n in prev:
                if n < width and y <= 0:  # moving north
                    gardens[x, y - 1].add(n + (width - 1) * width)
                if n % width == width - 1 and x >= 0:  # moving east
                    gardens[x + 1, y].add(n - width + 1)
                if n // width == width - 1 and y >= 0:  # moving south
                    gardens[x, y + 1].add(n % width)
                if n % width == 0 and x <= 0:  # moving west
                    gardens[x - 1, y].add(n + width - 1)
            # step within this garden
            reached = take_step(graph, prev)
            gardens[x, y].update(reached)
    return gardens


def take_step(graph, reached):
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


def calc(model):
    def tick(n=1):
        nonlocal taken, center, north, east, south, west, nw, ne, se, sw
        for _ in range(n):
            taken += 1
            center = take_step(graph, center)
            north = take_step(graph, north)
            east = take_step(graph, east)
            south = take_step(graph, south)
            west = take_step(graph, west)
            nw = take_step(graph, nw)
            ne = take_step(graph, ne)
            se = take_step(graph, se)
            sw = take_step(graph, sw)
        result[taken] = {
            "center": center,
            "north": north,
            "east": east,
            "south": south,
            "west": west,
            "nw": nw,
            "ne": ne,
            "se": se,
            "sw": sw,
        }

    start, graph, width = model
    half = width // 2
    result = {}

    # initial
    center = {start}
    # reached after 'half' steps
    north, east, south, west = get_edges(width)
    north, east, south, west = {north}, {east}, {south}, {west}
    # reached after 'width' steps
    nw, ne, se, sw = get_corners(width)
    nw, ne, se, sw = {nw}, {ne}, {se}, {sw}
    taken = 0
    tick(half)
    tick(width - half)
    tick(half)
    tick(width - half)
    return result


def part_two_calc(model, to_take=26_501_365):
    start, graph, width = model
    half = width // 2
    assert (
        to_take - half
    ) % width == 0, f"{to_take} ({(to_take - half) % width}) aint good"
    N = to_take // width
    assert N > 0, "must go at least one full round past the half"
    # after the initial half round and N full rounds:
    # 1 center tile, at 1.5 rounds
    # N-1 each cardinal tile, at 2 rounds
    # 1 each cardinal tile, at 1 round
    # triangle(N-2) each quadrant tile, at 2 rounds
    # N-1 each quadrant tile, at 1.5 rounds
    # N each quadrant tile, at .5 rounds

    result = calc(model)
    c = result[half]
    oneeighth_quad = len(c["nw"]) + len(c["ne"]) + len(c["se"]) + len(c["sw"])
    c = result[width]
    threequarter_cardinal = (
        len(c["north"]) + len(c["east"]) + len(c["south"]) + len(c["west"])
    )
    c = result[width + half]
    seveneighth_quad = len(c["nw"]) + len(c["ne"]) + len(c["se"]) + len(c["sw"])
    c = result[width * 2]
    cardinal = len(c["north"]) + len(c["east"]) + len(c["south"]) + len(c["west"])
    quad = len(c["nw"]) + len(c["ne"]) + len(c["se"]) + len(c["sw"])

    # print(f"center: {len(center)}")
    # print(f"north: {len(north)}")
    # print(f"east: {len(east)}")
    # print(f"south: {len(south)}")
    # print(f"west: {len(west)}")
    # print(f"quad: {quad}")
    print(to_string(model, c["center"]))
    return (
        len(c["center"])
        + (N - 1) * cardinal
        + threequarter_cardinal
        + triangle(N - 2) * quad
        + (N - 1) * seveneighth_quad
        + N * oneeighth_quad
    )


@functools.cache
def triangle(n):
    """The Nth triangle number: 1, 3, 6, 10, ..."""
    return n * (n + 1) // 2


def to_string(model, reached, tl=None, br=None):
    start, graph, width = model
    x1, y1 = tl if tl else (-1, -1)
    x2, y2 = br if br else (width, width)
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
    return "".join(sb)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two_calc,
    )

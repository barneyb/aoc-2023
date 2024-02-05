import functools

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
    draw(model, reached)
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


def part_two(model, to_take=26_501_365):
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

    # initial
    center = {start}
    # reached after 'half' steps
    north, east, south, west = get_edges(width)
    north, east, south, west = {north}, {east}, {south}, {west}
    # reached after 'width' steps
    nw, ne, se, sw = get_corners(width)
    nw, ne, se, sw = {nw}, {ne}, {se}, {sw}
    taken = 0
    for _ in range(half):
        taken += 1
        center = step(graph, center)
        north = step(graph, north)
        east = step(graph, east)
        south = step(graph, south)
        west = step(graph, west)
        nw = step(graph, nw)
        ne = step(graph, ne)
        se = step(graph, se)
        sw = step(graph, sw)
    oneeighth_quad = len(nw) + len(ne) + len(se) + len(sw)
    print(f"after {half}/{taken}, center is {len(center)}")
    for _ in range(half, width):
        taken += 1
        center = step(graph, center)
        north = step(graph, north)
        east = step(graph, east)
        south = step(graph, south)
        west = step(graph, west)
        nw = step(graph, nw)
        ne = step(graph, ne)
        se = step(graph, se)
        sw = step(graph, sw)
    threequarter_cardinal = len(north) + len(east) + len(south) + len(west)
    print(f"after {width}/{taken}, center is {len(center)}")
    for _ in range(half):
        taken += 1
        center = step(graph, center)
        north = step(graph, north)
        east = step(graph, east)
        south = step(graph, south)
        west = step(graph, west)
        nw = step(graph, nw)
        ne = step(graph, ne)
        se = step(graph, se)
        sw = step(graph, sw)
    center = len(center)
    print(f"after {width+half}/{taken}, center is {center}")
    seveneighth_quad = len(nw) + len(ne) + len(se) + len(sw)
    for _ in range(half, width):
        taken += 1
        north = step(graph, north)
        east = step(graph, east)
        south = step(graph, south)
        west = step(graph, west)
        nw = step(graph, nw)
        ne = step(graph, ne)
        se = step(graph, se)
        sw = step(graph, sw)
    cardinal = len(north) + len(east) + len(south) + len(west)
    quad = len(nw) + len(ne) + len(se) + len(sw)
    return (
        center
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


def draw(model, reached, tl=None, br=None):
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
    print("".join(sb))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

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
    return start, graph


def part_one(model):
    start, graph = model
    return (
        len(graph),
        sum(1 for adj in graph if adj is not None),
        sum(len(adj) for adj in graph if adj),
    )


# def part_two(model):
#     return None


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

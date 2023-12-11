from collections import Counter

from util import aoc


def parse(input):
    lines = input.splitlines()
    return len(lines[0]), len(lines), lines


def tick(model):
    def in_bounds(p):
        r, c = p
        return 0 <= r < h and 0 <= c < w

    def neighbors(w, h, p):
        r, c = p
        return filter(
            in_bounds,
            [
                (r - 1, c - 1),
                (r - 1, c),
                (r - 1, c + 1),
                (r, c + 1),
                (r + 1, c + 1),
                (r + 1, c),
                (r + 1, c - 1),
                (r, c - 1),
            ],
        )

    w, h, prev = model
    curr = []
    for r, line in enumerate(prev):
        cr = []
        for c, s in enumerate(line):
            hist = Counter(prev[a][b] for a, b in neighbors(w, h, (r, c)))
            match prev[r][c]:
                case ".":
                    cr.append("|" if hist["|"] >= 3 else ".")
                case "|":
                    cr.append("#" if hist["#"] >= 3 else "|")
                case "#":
                    cr.append("#" if hist["#"] and hist["|"] else ".")
        curr.append("".join(cr))
    return w, h, curr


def part_one(model):
    for _ in range(10):
        model = tick(model)
    _, _, lines = model
    hist = Counter()
    for l in lines:
        hist.update(l)
    return hist["|"] * hist["#"]


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

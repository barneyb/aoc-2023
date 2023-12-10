from collections import Counter

from util import aoc


class Map:
    def __init__(self, s):
        self.lines = s.splitlines()
        self.cols = len(self.lines[0])
        self.rows = len(self.lines)
        for r, l in enumerate(self.lines):
            c = l.find("S")
            if c < 0:
                continue
            self.start = (r, c)
            n = (r - 1, c)
            n = n in self and self[n] in "|7F"
            e = (r, c + 1)
            e = e in self and self[e] in "-J7"
            s = (r + 1, c)
            s = s in self and self[s] in "|JL"
            w = (r, c - 1)
            w = w in self and self[w] in "-LF"
            if n:
                c = "L" if e else "|" if s else "J"
            elif e:
                c = "F" if s else "-"
            else:
                c = "7"
            self.lines[r] = self.lines[r].replace("S", c)

    def __getitem__(self, p):
        r, c = p
        return self.lines[r][c]

    def __contains__(self, p):
        r, c = p
        return 0 <= r < self.rows and 0 <= c < self.cols

    def connected(self, p):
        r, c = p
        match self[p]:
            case "|":
                return [(r - 1, c), (r + 1, c)]
            case "-":
                return [(r, c - 1), (r, c + 1)]
            case "L":
                return [(r - 1, c), (r, c + 1)]
            case "J":
                return [(r - 1, c), (r, c - 1)]
            case "7":
                return [(r, c - 1), (r + 1, c)]
            case "F":
                return [(r, c + 1), (r + 1, c)]
            case _:
                raise RuntimeError(f"Unrecognized '{self[p]}' at {p}")


def get_path(m):
    prev = None
    curr = m.start
    path = []
    while True:
        path.append(curr)
        a, b = m.connected(curr)
        n = a if b == prev else b
        if n == m.start:
            return path
        prev, curr = curr, n


def part_one(m):
    return len(get_path(m)) // 2


def part_two(m):
    pipe = set(get_path(m))
    hist = Counter()
    for r, line in enumerate(m.lines):
        inside = False
        itr = enumerate(line)
        while True:
            try:
                c, p = next(itr)
            except StopIteration:
                break
            if (r, c) in pipe:
                if p in "LF":
                    while True:
                        _, p2 = next(itr)
                        if p2 == "-":
                            continue
                        if p2 == "7":
                            if p == "L":
                                inside = not inside
                        elif p2 == "J":
                            if p == "F":
                                inside = not inside
                        else:
                            raise RuntimeError(f"Unexpected '{p2}'")
                        break
                else:  # |
                    inside = not inside
            else:
                hist[inside] += 1
    return hist[True]


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Map,
        part_one,
        part_two,
    )

from util import aoc


def parse(input):
    patt = []
    patterns = [patt]
    for l in input.splitlines():
        if l == "":
            patt = []
            patterns.append(patt)
        else:
            patt.append(l)
    return patterns


def rotate_cw(patt):
    sbs = [[] for _ in patt[0]]
    for i in range(len(patt[0])):
        for l in patt:
            sbs[i].append(l[i])
    return ["".join(reversed(sb)) for sb in sbs]


def vert_line(patt):
    return horiz_line(rotate_cw(patt))


def horiz_line(patt):
    prev = None
    for i, l in enumerate(patt):
        if l == prev:
            n = min(i, len(patt) - i)
            reflects = True
            for j in range(n):
                if patt[i + j] != patt[i - j - 1]:
                    reflects = False
                    break
            if reflects:
                return i
        prev = l
    return -1


def part_one(patterns):
    total = 0
    for patt in patterns:
        h = horiz_line(patt)
        if h > 0:
            total += 100 * h
        else:
            v = vert_line(patt)
            total += v
    return total


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

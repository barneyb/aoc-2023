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


def vert_line(patt, *, smudges=0):
    return horiz_line(rotate_cw(patt), smudges=smudges)


def horiz_line(patt, *, smudges=0):
    def smudges_to_reflect(l, r):
        if not r:
            return len(l)
        if l == r:
            return 0
        return sum(1 for a, b in zip(l, r) if a != b) if smudged else 99999

    smudged = smudges > 0
    prev = None
    for i, line in enumerate(patt):
        ss = smudges_to_reflect(line, prev)
        if ss <= smudges:
            n = min(i, len(patt) - i)
            for j in range(1, n):
                ss += smudges_to_reflect(patt[i + j], patt[i - j - 1])
                if ss > smudges:
                    break
            if ss == smudges:
                return i
        prev = line
    return -1


def either_part(patterns, *, smudges=0):
    total = 0
    for patt in patterns:
        h = horiz_line(patt, smudges=smudges)
        if h > 0:
            total += 100 * h
        else:
            v = vert_line(patt, smudges=smudges)
            assert v > 0, f"Found no line of reflection in {patt}"
            total += v
    return total


def part_one(patterns):
    return either_part(patterns)


def part_two(patterns):
    return either_part(patterns, smudges=1)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

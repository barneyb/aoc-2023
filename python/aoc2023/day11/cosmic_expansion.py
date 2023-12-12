from util import aoc


def parse(input):
    return input.splitlines()


def expand(lines, factor=1):
    galaxies = []
    exs = []
    ex = 0
    for x in range(len(lines)):
        if all(l[x] == "." for l in lines):
            ex += factor - 1
        exs.append(ex)
        ex += 1
    ey = 0
    for l in lines:
        if l.find("#") < 0:
            ey += factor - 1
        else:
            x = -1
            while True:
                x = l.find("#", x + 1)
                if x < 0:
                    break
                galaxies.append((exs[x], ey))
        ey += 1
    return galaxies


def either_part(lines, expansion):
    total = 0
    galaxies = expand(lines, expansion)
    for i, (x1, y1) in enumerate(galaxies):
        for x2, y2 in galaxies[i + 1 :]:
            total += abs(x1 - x2) + abs(y1 - y2)
    return total


def part_one(lines):
    return either_part(lines, 2)


def part_two(lines):
    return either_part(lines, 1_000_000)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

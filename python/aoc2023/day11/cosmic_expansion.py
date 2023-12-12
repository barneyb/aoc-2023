from util import aoc


def parse(input):
    galaxies = []
    lines = input.splitlines()
    exs = []
    ex = 0
    for x in range(len(lines)):
        if all(l[x] == "." for l in lines):
            ex += 1
        exs.append(ex)
        ex += 1
    ey = 0
    for l in lines:
        if l.find("#") < 0:
            ey += 2
            continue
        x = -1
        while True:
            x = l.find("#", x + 1)
            if x < 0:
                break
            galaxies.append((exs[x], ey))
        ey += 1
    return galaxies


def part_one(galaxies):
    total = 0
    for i, a in enumerate(galaxies):
        for b in galaxies[i + 1 :]:
            total += abs(a[0] - b[0]) + abs(a[1] - b[1])
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

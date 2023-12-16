from util import aoc


def parse(input):
    return input.strip().split(",")


# noinspection PyPep8Naming
def HASH(s):
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h


def part_one(steps):
    return sum(HASH(s) for s in steps)


def part_two(steps):
    boxes = [{} for _ in range(256)]
    for sn in steps:
        if sn.endswith("-"):
            lbl = sn[:-1]
            b = boxes[HASH(lbl)]
            if lbl in b:
                del b[lbl]
        else:
            lbl = sn[:-2]
            boxes[HASH(lbl)][lbl] = int(sn[-1])
    total = 0
    for bn, b in enumerate(boxes):
        for sn, s in enumerate(b):
            total += (bn + 1) * (sn + 1) * b[s]
    return total


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

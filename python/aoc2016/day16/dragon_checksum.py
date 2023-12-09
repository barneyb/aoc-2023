from util import aoc


def gen(a):
    sb = [a, "0"]
    for c in reversed(a):
        sb.append("1" if c == "0" else "0")
    return "".join(sb)


def chksum(data):
    if len(data) % 2 == 1:
        return data
    sb = []
    for i in range(0, len(data), 2):
        sb.append("1" if data[i] == data[i + 1] else "0")
    return chksum("".join(sb))


def fill_and_chksum(seed, size):
    data = seed
    while len(data) < size:
        data = gen(data)
    return chksum(data[:size])


def part_one(seed):
    return fill_and_chksum(seed, 272)


def part_two(seed):
    return fill_and_chksum(seed, 35651584)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        None,
        part_one,
        part_two,
    )

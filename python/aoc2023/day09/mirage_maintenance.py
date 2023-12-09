from util import aoc


def parse(input):
    return [[int(n) for n in l.split()] for l in input.splitlines()]


def extrapolate(seq):
    """Returns a tuple of the predicted values before and after the sequence."""
    diffs = []
    all_same = True
    prev = seq[0]
    for n in seq[1:]:
        diffs.append(n - prev)
        all_same &= prev == n
        prev = n
    if all_same:
        return seq[0], seq[-1]
    else:
        f, l = extrapolate(diffs)
        return seq[0] - f, seq[-1] + l


def part_one(model):
    return sum(extrapolate(seq)[1] for seq in model)


def part_two(model):
    return sum(extrapolate(seq)[0] for seq in model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

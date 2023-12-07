from collections import Counter

from util import aoc


def parse(input):
    lines = input.splitlines()
    start = lines[0]
    rules = dict([l.split(" -> ") for l in lines[2:]])
    return (
        start[0],
        Counter([start[i : i + 2] for i in range(len(start) - 1)]),
        rules,
    )


def either_part(model, iterations):
    first, pairs, rules = model
    for _ in range(iterations):
        hist = Counter()
        for pair, n in pairs.items():
            c = rules[pair]
            hist[pair[0] + c] += n
            hist[c + pair[1]] += n
        pairs = hist
    elements = Counter()
    elements[first] = 1
    for pair, n in pairs.items():
        elements[pair[1]] += n
    mn = min(elements.values())
    mx = max(elements.values())
    return mx - mn


def part_one(model):
    return either_part(model, 10)


def part_two(model):
    return either_part(model, 40)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

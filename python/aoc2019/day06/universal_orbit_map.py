from util import aoc


def parse(input):
    return [tuple(l.split(")")) for l in input.splitlines()]


def part_one(model):
    lookup = dict((b, c) for c, b in model)
    cache = {"COM": 0}

    def walk(b):
        if b not in cache:
            n = walk(lookup[b]) + 1
            cache[b] = n
        return cache[b]

    for b in lookup.keys():
        walk(b)
    return sum(cache.values())


# def part_two(model):
#    return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

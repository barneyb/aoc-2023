from util import aoc


def parse(input):
    return build_paths((b, a) for a, b in (l.split(")") for l in input.splitlines()))


def build_paths(model):
    lookup = dict(model)
    paths = {"COM": []}

    def walk(b):
        if b not in paths:
            p = [b]
            p.extend(walk(lookup[b]))
            paths[b] = p
        return paths[b]

    for b in lookup.keys():
        walk(b)
    return paths


def part_one(paths):
    return sum(len(p) for p in paths.values())


def part_two(paths):
    you = paths["YOU"][1:]
    san = paths["SAN"][1:]
    lookup = set(san)
    for b in you:
        if b in lookup:
            return you.index(b) + san.index(b)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

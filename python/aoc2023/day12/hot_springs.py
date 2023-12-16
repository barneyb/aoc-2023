import re

from util import aoc


def parse(input):
    return [
        (ss, [int(g) for g in gs.split(",")])
        for ss, gs in (l.split(" ") for l in input.splitlines())
    ]


def arrangements(springs: str, groups):
    def gen(springs):
        idx = springs.find("?")
        if idx < 0:
            yield springs
        else:
            prefix = springs[:idx]
            suffix = springs[idx + 1 :]
            yield from gen(prefix + "." + suffix)
            yield from gen(prefix + "#" + suffix)

    parts = [r"\.*"]
    parts.extend(r"\.+".join(r"#{" + str(g) + "}" for g in groups))
    parts.append(r"\.*")
    test = re.compile("".join(parts))
    return sum(1 for s in gen(springs) if test.fullmatch(s))


def part_one(model):
    return sum(arrangements(s, gs) for s, gs in model)


# def part_two(model):
#     return len(model)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

from util import aoc


# rfg{s<537:gd,x>2440:R,A}
def parse_workflow(line: str):
    idx = line.index("{")
    name = line[0:idx]
    *branches, fallthrough = line[idx + 1 : -1].split(",")
    return (
        name,
        [(s[0], s[1], int(s[2:]), d) for s, d in (b.split(":") for b in branches)],
        fallthrough,
    )


# {x=1679,m=44,a=2067,s=496}
def parse_part(line):
    return {a[0]: int(a[2:]) for a in line[1:-1].split(",")}


def parse(input):
    workflows = {}
    parts = []
    in_parts = False
    for line in input.splitlines():
        if line == "":
            in_parts = True
        elif in_parts:
            parts.append(parse_part(line))
        else:
            n, bs, f = parse_workflow(line)
            workflows[n] = (bs, f)
    return workflows, parts


def evaluate(workflow, part):
    branches, fallthrough = workflow
    for a, op, n, out in branches:
        v = part[a]
        if v < n if op == "<" else v > n:
            return out
    return fallthrough


def accept(workflows, part):
    curr = "in"
    while curr not in "RA":
        curr = evaluate(workflows[curr], part)
    return curr == "A"


def part_one(model):
    workflows, parts = model
    return sum(sum(p.values()) for p in parts if accept(workflows, p))


# def part_two(model):
#     return None


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

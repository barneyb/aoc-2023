import operator
from collections import deque
from functools import reduce

from util import aoc


# rfg{s<537:gd,x>2440:R,A}
def parse_workflow(line: str):
    idx = line.index("{")
    name = line[0:idx]
    *bs, fallthrough = line[idx + 1 : -1].split(",")
    bs = [(s[0], s[1], int(s[2:]), d) for s, d in (b.split(":") for b in bs)]
    # if the last branch selects the fallthrough, discard it
    while len(bs) and bs[-1][3] == fallthrough:
        bs = bs[:-1]
    # half-open ranges are rather easier to work with, so change > to ≥
    bs = [(a, op, n, d) if op == "<" else (a, "≥", n + 1, d) for a, op, n, d in bs]
    return name, bs, fallthrough


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
        if v < n if op == "<" else v >= n:
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


def eval_many(workflow, parts):
    branches, fallthrough = workflow
    for a, op, n, out in branches:
        s, e = parts[a]
        if op == "<":
            if s >= n:
                continue  # all above
            if e < n:
                yield out, parts
                return  # all below
            gs, ge = s, n
            bs, be = n, e
        else:  # op == "≥"
            if e <= n:
                continue  # all below
            if s > n:
                yield out, parts
                return  # all above
            gs, ge = n, e
            bs, be = s, n
        if gs < ge:
            temp = parts.copy()
            temp[a] = gs, ge
            yield out, temp
            del temp, gs, ge
        if bs >= be:
            return
        parts[a] = bs, be
    yield fallthrough, parts


def count_parts(parts):
    return reduce(operator.mul, (e - s for s, e in parts.values()))


def part_two(model):
    workflows, _ = model
    r = (1, 4001)
    all_parts = {"x": r, "m": r, "a": r, "s": r}
    stack = deque()
    stack.append(("in", all_parts))
    accepted = 0
    while len(stack):
        wfn, parts = stack.pop()
        if wfn == "R":
            continue
        if wfn == "A":
            accepted += count_parts(parts)
            continue
        stack.extend(eval_many(workflows[wfn], parts))
    return accepted


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

from collections import deque

from util import aoc
from util.geom_2d import move


def parse_dir(c):
    match c:
        case "U" | "3":
            return 0
        case "R" | "0":
            return 1
        case "D" | "1":
            return 2
        case "L" | "2":
            return 3


def parse(input):
    return [
        (parse_dir(d), int(n), c[1:-1])
        for d, n, c in [l.split() for l in input.splitlines()]
    ]


def get_corners(plan):
    x, y = 0, 0
    corners = []
    prev_dirs = deque([plan[-1][0]], maxlen=2)
    for d, n in plan:
        if len(prev_dirs) == 2 and prev_dirs[0] != d:  # a 180
            pd = prev_dirs[1]
            if (pd + 1) % 4 == d:  # right
                x, y = move((x, y), pd, 1)
            else:  # left
                x, y = move((x, y), pd, -1)
        prev_dirs.append(d)
        corners.append((x, y))
        x, y = move((x, y), d, n)
    return corners


def get_rules(corners):
    """Returns the horizontal rules in the loop as (y, start_x, end_x) tuples."""
    (x1, _), (x2, _) = corners[0:2]
    if x1 == x2:  # rotate so horiz first
        first, *corners = corners
        corners.append(first)
    rules = []
    for i in range(0, len(corners), 2):
        a, b = corners[i : i + 2]
        (x1, y), (x2, _) = a, b
        if x2 < x1:
            x2, x1 = x1, x2
        rules.append((y, x1, x2))
    rules.sort()
    return rules


def overlap(q, r):
    """Given two start:end tuples, return a tuple containing their overlap"""
    if r < q:
        q, r = r, q
    qs, qe = q
    rs, re = r
    if qe <= rs:  # no overlap
        return qs, qs
    return rs, re if re < qe else qe


def either_part(plan):
    area = 0
    blocks = []  # x-ranges w/ known top, but no bottom yet
    for ry, rs, re in get_rules(get_corners(plan)):
        next_blocks = []
        covered_pieces = []
        for by, bs, be in blocks:
            os, oe = overlap((bs, be), (rs, re))
            if os < oe:  # something terminated!
                area += (oe - os) * (ry - by)
                covered_pieces.append((os, oe))
                if bs < os:
                    next_blocks.append((by, bs, min(be, os)))
                if be > oe:
                    next_blocks.append((by, max(bs, oe), be))
            else:
                next_blocks.append((by, bs, be))
        covered_pieces.sort()
        x = rs
        for s, e in covered_pieces:
            if x < s:
                next_blocks.append((ry, x, s))
            x = e
        if x < re:
            next_blocks.append((ry, x, re))
        blocks = next_blocks
    return area


def part_one(model):
    return either_part([(d, n) for d, n, _ in model])


def parse_color(c):
    return parse_dir(c[-1]), int(c[1:-1], 16)


def reparse(model):
    return [parse_color(c) for _, _, c in model]


def part_two(model):
    return either_part(reparse(model))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

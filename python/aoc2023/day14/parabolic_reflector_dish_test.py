from .parabolic_reflector_dish import *

# fmt: off
EXAMPLE = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

PARSE_EXAMPLE="""\
O.#
#OO
"""
PARSE_MODEL = (3, 2, {(0, 0): "O",
                      (2, 0): "#",
                      (0, 1): "#",
                      (1, 1): "O",
                      (2, 1): "O",
                     })
# fmt: on

MODEL = parse(EXAMPLE)


def unparse(model):
    w, h, rocks = model
    sb = []
    for y in range(h):
        for x in range(w):
            p = (x, y)
            sb.append(rocks[p] if p in rocks else ".")
        sb.append("\n")
    return "".join(sb)


def test_parse():
    assert parse(PARSE_EXAMPLE) == PARSE_MODEL
    assert unparse(PARSE_MODEL) == PARSE_EXAMPLE


def test_example_two():
    curr = MODEL
    assert unparse(curr) == EXAMPLE
    curr = spin_cycle(curr)
    assert (
        unparse(curr)
        == """\
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
"""
    )
    curr = spin_cycle(curr)
    assert (
        unparse(curr)
        == """\
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
"""
    )
    curr = spin_cycle(curr)
    assert (
        unparse(curr)
        == """\
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
"""
    )


def test_part_one():
    assert part_one(MODEL) == 136


def test_part_two():
    assert part_two(MODEL) == 64

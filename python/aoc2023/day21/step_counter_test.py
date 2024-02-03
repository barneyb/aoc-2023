from .step_counter import *

EXAMPLE = """\
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def test_parse():
    start, graph = parse(EXAMPLE)
    assert start == 60
    assert graph[start] == [59, 49]


def test_part_one():
    assert part_one(parse(EXAMPLE), 6) == 16


# def test_part_two():
#     assert part_two(MODEL) == 1_234

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

EXAMPLE_TWO = """\
...........
..#...##.#.
.###..#..#.
..#.#...#..
....#.#....
.....S.....
.##......#.
....#..##..
.##.#.####.
.##...#.##.
...........
"""

MODEL = parse(EXAMPLE)
MODEL_TWO = parse(EXAMPLE_TWO)


def test_parse():
    start, graph, width = MODEL
    assert start == 60
    assert graph[start] == [59, 49]
    assert width == 11


def test_part_one():
    assert part_one(MODEL, 6) == 16


def test_get_edges():
    north, east, south, west = get_edges(11)
    assert north == 5
    assert east == 65
    assert south == 115
    assert west == 55


def test_get_corners():
    nw, ne, se, sw = get_corners(11)
    assert nw == 0
    assert ne == 10
    assert se == 120
    assert sw == 110


def test_part_two_6():
    assert part_two(MODEL_TWO, 6) == 36


def test_part_two_10():
    assert part_two(MODEL_TWO, 10) == 88


def test_part_two_50():
    assert part_two(MODEL_TWO, 50) == 1904


def test_part_two_100():
    print()
    assert part_two(MODEL_TWO, 100) == 7465
    assert part_two(MODEL_TWO, 101) == 7594


def test_part_two_200():
    print()
    assert part_two(MODEL_TWO, 200) == 29599

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
.#.#..#..#.
..#.#...#..
....#.#....
.....S.....
.##......#.
....#..##..
.##.#...##.
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
    print()
    # assert part_two(MODEL_TWO, 0) == 1
    # assert part_two(MODEL_TWO, 1) == 4
    # assert part_two(MODEL_TWO, 2) == 7
    # assert part_two(MODEL_TWO, 3) == 14
    # assert part_two(MODEL_TWO, 4) == 19
    # assert part_two(MODEL_TWO, 5) == 26  # N=0
    # assert part_two(MODEL_TWO, 6) == 38
    # assert part_two(MODEL_TWO, 7) == 47
    # assert part_two(MODEL_TWO, 8) == 63
    assert part_two(MODEL_TWO, 16) == 215  # N=1
    assert part_two(MODEL_TWO, 27) == 586  # N=2
    # assert part_two(MODEL_TWO, 33) == 853
    assert part_two(MODEL_TWO, 38) == 1139  # N=3


def test_triangle():
    assert triangle(0) == 0
    assert triangle(1) == 1
    assert triangle(2) == 3
    assert triangle(3) == 6
    assert triangle(4) == 10
    assert triangle(5) == 15
    assert triangle(6) == 21


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

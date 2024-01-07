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

GARDEN = Garden(EXAMPLE)


def test_unparse():
    assert str(GARDEN) == EXAMPLE


def test_part_one():
    assert part_one(GARDEN, 6) == 16


def test_part_two_6():
    assert part_two(GARDEN, 6) == 16


def test_part_two_10():
    assert part_two(GARDEN, 10) == 50


def test_part_two_50():
    assert part_two(GARDEN, 50) == 1594


def test_part_two_100():
    assert part_two(GARDEN, 100) == 6536


# def test_part_two_500():
#     assert part_two(GARDEN, 500) == 167004


# def test_part_two_1000():
#     assert part_two(GARDEN, 1000) == 668697


# def test_part_two_5000():
#     assert part_two(GARDEN, 5000) == 16733044

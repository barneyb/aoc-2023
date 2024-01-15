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

GARDEN = Garden(EXAMPLE)
GARDEN_TWO = Garden(EXAMPLE_TWO)


def test_unparse():
    assert str(GARDEN) == EXAMPLE


def test_part_one():
    assert part_one(GARDEN, 6) == 16
    assert part_one(GARDEN_TWO, 6) == 36


def test_part_two_6():
    assert part_two(GARDEN, 6) == 16
    assert part_two(GARDEN_TWO, 6) == 36


def test_part_two_10():
    assert part_two(GARDEN, 10) == 50
    assert part_two(GARDEN_TWO, 10) == 88


def test_part_two_50():
    # assert part_two(GARDEN, 50) == 1594
    assert part_two(GARDEN_TWO, 50) == 1904


def test_part_two_100():
    print()
    # assert part_two(GARDEN, 100) == 6536
    assert part_two(GARDEN_TWO, 100) == 7465
    # assert part_two(GARDEN, 101) == 6684
    # assert part_two(GARDEN_TWO, 101) == 7594


# def test_part_two_200():
#     print()
#     assert part_two(GARDEN, 200) == 26538
#     assert part_two(GARDEN_TWO, 200) == 29599


# def test_part_two_500():
#     assert part_two(GARDEN, 500) == 167004


# def test_part_two_1000():
#     assert part_two(GARDEN, 1000) == 668697


# def test_part_two_5000():
#     assert part_two(GARDEN, 5000) == 16733044

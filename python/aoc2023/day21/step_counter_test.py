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


def test_part_one():
    assert part_one(GARDEN, 6) == 16


# def test_part_two():
#     assert part_two(GARDEN) == 1_234

from .step_counter import *

# fmt: off
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

MODEL = ["so", 
         "many", 
         "lines",
        ]
# fmt: on


def test_parse():
    start, graph = parse(EXAMPLE)
    assert start == 60
    assert graph[start] == [59, 49]


def test_part_one():
    assert part_one(MODEL) == 7_654


# def test_part_two():
#     assert part_two(MODEL) == 1_234

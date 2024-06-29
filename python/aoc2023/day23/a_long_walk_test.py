from .a_long_walk import *

EXAMPLE = """\
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""


def test_parse():
    trails = Trails(EXAMPLE)
    assert trails.width == 23
    assert trails.to_coords(trails.start) == (1, 0)
    assert trails.to_coords(trails.goal) == (21, 22)


def test_find_forks():
    trails = Trails(EXAMPLE)
    forks = [trails.to_coords(f) for f in find_forks(trails)]
    assert (3, 5) in forks
    assert (5, 13) in forks
    assert (21, 11) in forks
    assert len(forks) == 7  # and a few others


def test_part_one():
    assert part_one(EXAMPLE) == 94


def test_part_two():
    assert part_two(EXAMPLE) == 154

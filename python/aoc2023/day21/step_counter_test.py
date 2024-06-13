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
    assert part_one(MODEL, 0) == 1
    assert part_one(MODEL, 1) == 2
    assert part_one(MODEL, 2) == 4
    assert part_one(MODEL, 3) == 6
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


def test_part_two_simulate():
    # sb = []
    # for y in range(11):
    #     sb.append("\n")
    #     for x in range(11):
    #         sb.append(f"{(y*11+x):>4}")
    # print("".join(sb))
    assert part_two_simulate(MODEL, 0) == 1
    assert part_two_simulate(MODEL, 1) == 2
    assert part_two_simulate(MODEL, 2) == 4
    assert part_two_simulate(MODEL, 3) == 6
    assert part_two_simulate(MODEL, 5) == 13
    assert part_two_simulate(MODEL, 6) == 16
    assert part_two_simulate(MODEL, 10) == 50
    assert part_two_simulate(MODEL, 50) == 1594
    assert part_two_simulate(MODEL, 100) == 6536
    # assert part_two_simulate(MODEL, 200) == 26538
    # assert part_two_simulate(MODEL, 500) == 167004
    # assert part_two_simulate(MODEL, 1000) == 668697
    # assert part_two_simulate(MODEL, 5000) == 16733044
    assert part_two_simulate(MODEL_TWO, 0) == 1
    assert part_two_simulate(MODEL_TWO, 1) == 4
    assert part_two_simulate(MODEL_TWO, 2) == 7
    assert part_two_simulate(MODEL_TWO, 3) == 14
    assert part_two_simulate(MODEL_TWO, 5) == 26
    assert part_two_simulate(MODEL_TWO, 6) == 38
    assert part_two_simulate(MODEL_TWO, 10) == 90
    assert part_two_simulate(MODEL_TWO, 50) == 1954
    assert part_two_simulate(MODEL_TWO, 100) == 7627
    # assert part_two_simulate(MODEL_TWO, 200) == 30265


# def test_part_two():
#     print()
#     _, _, width = MODEL_TWO
#     half = width // 2
#     for n in range(1, 4):
#         steps = width * n + half
#         sim = part_two_simulate(MODEL_TWO, steps)
#         calc = part_two_calc(MODEL_TWO, steps)
#         assert sim == calc, f"failed at N={n}"


def test_triangle():
    assert triangle(0) == 0
    assert triangle(1) == 1
    assert triangle(2) == 3
    assert triangle(3) == 6
    assert triangle(4) == 10
    assert triangle(5) == 15
    assert triangle(6) == 21

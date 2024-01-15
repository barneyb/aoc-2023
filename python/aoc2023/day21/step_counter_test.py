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


# after 28 steps: 25 gardens w/ 614 positions
#                 │                               │                               │
#                 1                               D                              28
#             6  40   9                       F   D   G                      23  17  23
#         6  43  42  44   9               F   F   D   G   G              23  12   6  12  23
# ─   1  40  42  47  42  39   1   ─   C   C   C   A   E   E   E   ─  28  17   6   0   6  17  28   ─
#         9  44  42  42   8               H   H   B   I   I              23  12   6  12  23
#             9  39   8                       H   B   I                      23  17  23
#                 1                               B                              28
#                 │                               │                               │
#               cnt                             type                            turn
#
# after 39 steps: 41 gardens w/ 1170 positions
#                     │                                       │                                       │
#                     1                                       D                                      39
#                 6  40   9                               F   D   G                              34  28  34
#             6  43  42  44   9                       F   F   D   G   G                      34  23  17  23  34
#         6  43  42  47  42  44   9               F   F   F   D   G   G   G              34  23  12   6  12  23  34
# ─   1  40  42  47  42  47  42  39   1   ─   C   C   C   C   A   E   E   E   E   ─  39  28  17   6   0   6  17  28  39   ─
#         9  44  42  47  42  42   8               H   H   H   B   I   I   I              34  23  12   6  12  23  34
#             9  44  42  42   8                       H   H   B   I   I                      34  23  17  23  34
#                 9  39   8                               H   B   I                              34  28  34
#                     1                                       B                                      39
#                     │                                       │                                       │
#                   cnt                                     type                                    turn
#
# after 50 steps: 61 gardens w/ 1904 positions
#                         │                                               │                                               │
#                         1
#                     6  40   9                                       F   D   G                                      45  39  45
#                 6  43  42  44   9                               F   F   D   G   G                              45  34  28  34  45
#             6  43  42  47  42  44   9                       F   F   F   D   G   G   G                      45  34  23  17  23  34  45
#         6  43  42  47  42  47  42  44   9               F   F   F   F   D   G   G   G   G              45  34  23  12   6  12  23  34  45
# ─   1  40  42  47  42  47  42  47  42  39   1   ─       C   C   C   C   A   E   E   E   E       ─      39  28  17   6   0   6  17  28  39       ─
#         9  44  42  47  42  47  42  42   8               H   H   H   H   B   I   I   I   I              45  34  23  12   6  12  23  34  45
#             9  44  42  47  42  42   8                       H   H   H   B   I   I   I                      45  34  23  17  23  34  45
#                 9  44  42  42   8                               H   H   B   I   I                              45  34  28  34  45
#                     9  39   8                                       H   B   I                                      45  39  45
#                         1
#                         │                                               │                                               │
#                       cnt                                             type                                            turn
#
# after 61 steps: 85 gardens w/ 2816 positions
#                             │                                                       │                                                       │
#                             1                                                       D                                                      61
#                         6  40   9                                               F   D   G                                              56  50  56
#                     6  43  42  44   9                                       F   F   D   G   G                                      56  45  39  45  56
#                 6  43  42  47  42  44   9                               F   F   F   D   G   G   G                              56  45  34  28  34  45  56
#             6  43  42  47  42  47  42  44   9                       F   F   F   F   D   G   G   G   G                      56  45  34  23  17  23  34  45  56
#         6  43  42  47  42  47  42  47  42  44   9               F   F   F   F   F   D   G   G   G   G   G              56  45  34  23  12   6  12  23  34  45  56
# ─   1  40  42  47  42  47  42  47  42  47  42  39   1   ─   C   C   C   C   C   C   A   E   E   E   E   E   E   ─  61  50  39  28  17   6   0   6  17  28  39  50  61   ─
#         9  44  42  47  42  47  42  47  42  42   8               H   H   H   H   H   B   I   I   I   I   I              56  45  34  23  12   6  12  23  34  45  56
#             9  44  42  47  42  47  42  42   8                       H   H   H   H   B   I   I   I   I                      56  45  34  23  17  23  34  45  56
#                 9  44  42  47  42  42   8                               H   H   H   B   I   I   I                              56  45  34  28  34  45  56
#                     9  44  42  42   8                                       H   H   B   I   I                                      56  45  39  45  56
#                         9  39   8                                               H   B   I                                              56  50  56
#                             1                                                       B                                                      61
#                             │                                                       │                                                       │
#                           cnt                                                     type                                                    turn

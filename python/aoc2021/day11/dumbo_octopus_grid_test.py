from .dumbo_octopus_grid import *

# fmt: off
EXAMPLE_ONE_A = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

EXAMPLE_ONE_B = """11111
19991
19191
19991
11111
"""

MODEL_ONE_B = (5, 5, [[1,1,1,1,1],
                      [1,9,9,9,1],
                      [1,9,1,9,1],
                      [1,9,9,9,1],
                      [1,1,1,1,1]])
# fmt: on


def test_parse():
    assert parse(EXAMPLE_ONE_B) == MODEL_ONE_B


def test_unparse():
    assert unparse(MODEL_ONE_B) == EXAMPLE_ONE_B


def test_example_1b():
    step1, flashes = tick(parse(EXAMPLE_ONE_B))
    assert (
        unparse(step1)
        == """34543
40004
50005
40004
34543
"""
    )
    assert flashes == 9

    step2, flashes = tick(step1)
    assert (
        unparse(step2)
        == """45654
51115
61116
51115
45654
"""
    )
    assert flashes == 0


def test_example_1a():
    curr = parse(EXAMPLE_ONE_A)
    for _ in range(10):
        curr, _ = tick(curr)
    assert (
        unparse(curr)
        == """0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000
"""
    )


def test_part_one_10_steps():
    model = parse(EXAMPLE_ONE_A)
    assert part_one(model, steps=10) == 204


def test_part_one_full():
    model = parse(EXAMPLE_ONE_A)
    assert part_one(model) == 1656

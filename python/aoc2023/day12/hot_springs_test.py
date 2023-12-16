from .hot_springs import *

# fmt: off
EXAMPLE = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

MODEL = [
    ("???.###", (1, 1, 3)),
    (".??..??...?##.", (1, 1, 3)),
    ("?#?#?#?#?#?#?#?", (1, 3, 1, 6)),
    ("????.#...#...", (4, 1, 1)),
    ("????.######..#####.", (1, 6, 5)),
    ("?###????????", (3, 2, 1)),
]
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_arrangements():
    assert arrangements(MODEL[0]) == 1
    assert arrangements(MODEL[1]) == 4
    assert arrangements(MODEL[2]) == 1
    assert arrangements(MODEL[3]) == 1
    assert arrangements(MODEL[4]) == 4
    assert arrangements(MODEL[5]) == 10
    assert arrangements(("??????#.?#####??", (1, 1, 1, 6))) == 12


def test_part_one():
    assert part_one(MODEL) == 21


def test_unfold():
    assert unfold((".#", [1])) == (".#?.#?.#?.#?.#", [1, 1, 1, 1, 1])
    assert unfold(("???.###", [1, 1, 3])) == (
        "???.###????.###????.###????.###????.###",
        [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3],
    )


def test_unfolded_arrangements():
    assert arrangements(unfold(MODEL[0])) == 1
    assert arrangements(unfold(MODEL[3])) == 16
    assert arrangements(unfold(("??????#.?#####??", (1, 1, 1, 6)))) == 4687500


def test_part_two():
    assert part_two(MODEL[0:1]) == 1
    assert part_two(MODEL) == 525152

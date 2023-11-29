from calorie_counting import *

EXAMPLE_ONE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_part_one():
    assert part_one(EXAMPLE_ONE) == 24_000

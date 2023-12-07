from .block_print import *

ZUKCJ = """\
####.#..#.#..#..##....##.
...#.#..#.#.#..#..#....#.
..#..#..#.##...#.......#.
.#...#..#.#.#..#.......#.
#....#..#.#.#..#..#.#..#.
####..##..#..#..##...##.."""

ZJHRKCPLYJ = """
████   ██ █  █ ███  █  █  ██  ███  █    █   █  ██ 
   █    █ █  █ █  █ █ █  █  █ █  █ █    █   █   █ 
  █     █ ████ █  █ ██   █    █  █ █     █ █    █ 
 █      █ █  █ ███  █ █  █    ███  █      █     █ 
█    █  █ █  █ █ █  █ █  █  █ █    █      █  █  █ 
████  ██  █  █ █  █ █  █  ██  █    ████   █   ██  
"""


# noinspection PyPep8Naming
def test_read_ZUKCJ():
    assert read(ZUKCJ) == "ZUKCJ"


# noinspection PyPep8Naming
def test_read_ZJHRKCPLYJ():
    assert read(ZJHRKCPLYJ) == "ZJHRKCPLYJ"

from two_factor_authentication import *

EXAMPLE = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""

MODEL = [
    ("rect", 3, 2),
    ("col", 1, 1),
    ("row", 0, 4),
    ("col", 1, 1),
]


def test_parse():
    assert parse(EXAMPLE) == MODEL


def parse_screen(string):
    width = 0
    height = 0
    pixels = []
    x = 0
    for c in string:
        match c:
            case "\n":
                if width == 0:
                    width = x
                else:
                    assert x == width
                height += 1
                x = 0
            case "#":
                x += 1
                pixels.append(True)
            case ".":
                x += 1
                pixels.append(False)
            case _:
                raise RuntimeError(f"Unknown '{c}' in input")
    if x > 0:
        # no final newline
        height += 1
    assert len(pixels) == width * height
    screen = Screen(width, height)
    screen.pixels = pixels  # EGADS!!
    return screen


def test_rect():
    screen = Screen(7, 3)
    screen.execute([("rect", 3, 2)])
    assert (
        screen.__str__()
        == """###....
###....
......."""
    )


def test_col():
    screen = parse_screen(
        """###....
###....
......."""
    )
    screen.execute([("col", 1, 1)])
    assert (
        screen.__str__()
        == """#.#....
###....
.#....."""
    )


def test_row():
    screen = parse_screen(
        """###....
###....
......."""
    )
    screen.execute([("row", 0, 1)])
    assert (
        screen.__str__()
        == """.###...
###....
......."""
    )


def test_col_wrap():
    screen = parse_screen(
        """#######
#######
#.#####"""
    )
    screen.execute(
        [("col", 1, 1)],
    )
    assert (
        screen.__str__()
        == """#.#####
#######
#######"""
    )


def test_row_wrap():
    screen = parse_screen(
        """###....
###....
......."""
    )
    screen.execute([("row", 0, 5)])
    assert (
        screen.__str__()
        == """#....##
###....
......."""
    )


def test_example_one():
    screen = Screen(7, 3)
    screen.execute(MODEL)
    assert screen.lit_pixel_count() == 6
    assert (
        screen.__str__()
        == """.#..#.#
#.#....
.#....."""
    )

from two_factor_authentication import *

EXAMPLE = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""

MODEL = [("rect", 3, 2),
         ("col", 1, 1),
         ("row", 0, 4),
         ("col", 1, 1)]


def test_parse():
    assert parse(EXAMPLE) == MODEL


def parse_display(str):
    width = 0
    height = 0
    display = []
    x = 0
    for c in str:
        match c:
            case '\n':
                if width == 0:
                    width = x
                else:
                    assert x == width
                height += 1
                x = 0
            case '#':
                x += 1
                display.append(True)
            case '.':
                x += 1
                display.append(False)
    if x > 0:
        # no final newline
        height += 1
    assert len(display) == width * height
    return display, width, height


def test_rect():
    d = build_and_execute([("rect", 3, 2)], 7, 3)
    assert to_string(d, 7, 3) == """###....
###....
......."""


def test_col():
    display, width, height = parse_display("""###....
###....
.......""")
    display = execute(display, [('col', 1, 1)], width, height)
    assert to_string(display, width, height) == """#.#....
###....
.#....."""


def test_row():
    display, width, height = parse_display("""###....
###....
.......""")
    display = execute(display, [('row', 0, 1)], width, height)
    assert to_string(display, width, height) == """.###...
###....
......."""


def test_col_wrap():
    display, width, height = parse_display("""#######
#######
#.#####""")
    display = execute(display, [('col', 1, 1)], width, height)
    assert to_string(display, width, height) == """#.#####
#######
#######"""


def test_row_wrap():
    display, width, height = parse_display("""###....
###....
.......""")
    display = execute(display, [('row', 0, 5)], width, height)
    assert to_string(display, width, height) == """#....##
###....
......."""


def test_part_one():
    display = build_and_execute(MODEL, 7, 3)
    print(f"\n{to_string(display, 7, 3)}")
    assert lit_pixel_count(display) == 6

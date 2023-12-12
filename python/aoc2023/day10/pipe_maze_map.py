from PIL import Image, ImageDraw

import aoc2023.day10 as maze
from util import aoc

GROUND_IN = "#000099"
GROUND_OUT = "#006600"
GROUND_LOOP = "#990000"
PIPE = "#9999aa"
PX = 1
PITCH = 5 * PX


def fill(draw, p, color):
    r, c = p
    x = c * PITCH
    y = r * PITCH
    draw.rectangle((x, y, x + PITCH - 1, y + PITCH - 1), color)


def tall(draw, x, y, color):
    draw.rectangle((x, y, x + PX - 1, y + 3 * PX - 1), color)


def wide(draw, x, y, color):
    draw.rectangle((x, y, x + 3 * PX - 1, y + PX - 1), color)


def lay(draw, p, sym, color):
    r, c = p
    x = c * PITCH
    y = r * PITCH
    if sym in "|LJ":  # top
        wide(draw, x + PX, y, color)
        tall(draw, x + 2 * PX, y, color)
    if sym in "|F7":  # bottom
        wide(draw, x + PX, y + 4 * PX, color)
        tall(draw, x + 2 * PX, y + 2 * PX, color)
    if sym in "-J7":  # left
        wide(draw, x, y + 2 * PX, color)
        tall(draw, x, y + 1 * PX, color)
    if sym in "-FL":  # right
        wide(draw, x + 2 * PX, y + 2 * PX, color)
        tall(draw, x + 4 * PX, y + 1 * PX, color)


if __name__ == "__main__":
    data = aoc.get_input(__file__)
    m = maze.Map(data)
    path = maze.get_path(m)
    pipe = set(path)
    inside = maze.get_inside(m, pipe)

    im = Image.new(mode="RGB", size=(m.cols * PITCH, m.rows * PITCH), color=GROUND_OUT)
    draw = ImageDraw.Draw(im)
    for p, c in m.points():
        if p in pipe:
            fill(draw, p, GROUND_LOOP)
            lay(draw, p, c, PIPE)
        elif p in inside:
            fill(draw, p, GROUND_IN)
            if c != ".":
                lay(draw, p, c, PIPE)
        elif c != ".":
            lay(draw, p, c, PIPE)
    fill(draw, m.start, "#ffff00")
    fill(draw, path[len(path) // 2], "#ff9900")

    im.show()

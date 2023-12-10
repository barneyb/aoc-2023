from PIL import Image, ImageDraw

import aoc2023.day10 as maze
from util import aoc

GROUND_IN = "#000099"
GROUND_OUT = "#006600"
GROUND_LOOP = "#990000"
PIPE_IN = "#9999FF"
PIPE_OUT = "#99FF99"
PIPE_LOOP = "#FF9999"
PX = 1
PITCH = 5 * PX


def fill(draw, p, color):
    r, c = p
    x = c * PITCH
    y = r * PITCH
    draw.rectangle((x, y, x + PITCH - 1, y + PITCH - 1), color)


def lay(draw, p, sym, color):
    r, c = p
    x = c * PITCH
    y = r * PITCH
    if sym in "|LJ":  # top
        draw.rectangle(
            ((x + PX, y), (x + 4 * PX - 1, y + PX - 1)),
            color,
        )
        draw.rectangle(
            ((x + 2 * PX, y), (x + 3 * PX - 1, y + 3 * PX - 1)),
            color,
        )
    if sym in "|F7":  # bottom
        draw.rectangle(
            ((x + PX, y + 4 * PX), (x + 4 * PX - 1, y + 5 * PX - 1)),
            color,
        )
        draw.rectangle(
            ((x + 2 * PX, y + 2 * PX), (x + 3 * PX - 1, y + 5 * PX - 1)),
            color,
        )
    if sym in "-J7":  # left
        draw.rectangle(
            ((x, y + PX), (x + PX - 1, y + 4 * PX - 1)),
            color,
        )
        draw.rectangle(
            ((x, y + 2 * PX), (x + 3 * PX - 1, y + 3 * PX - 1)),
            color,
        )
    if sym in "-FL":  # right
        draw.rectangle(
            ((x + 4 * PX, y + PX), (x + 5 * PX - 1, y + 4 * PX - 1)),
            color,
        )
        draw.rectangle(
            ((x + 2 * PX, y + 2 * PX), (x + 5 * PX - 1, y + 3 * PX - 1)),
            color,
        )


if __name__ == "__main__":
    data = aoc.get_input(__file__)
    m = maze.Map(data)
    pipe = set(maze.get_path(m))
    inside = maze.get_inside(m, pipe)

    im = Image.new(mode="RGB", size=(m.cols * PITCH, m.rows * PITCH), color=GROUND_OUT)
    draw = ImageDraw.Draw(im)
    for p, c in m.points():
        if p in pipe:
            fill(draw, p, GROUND_LOOP)
            lay(draw, p, c, PIPE_LOOP)
        elif p in inside:
            fill(draw, p, GROUND_IN)
            if c != ".":
                lay(draw, p, c, PIPE_IN)
        elif c != ".":
            lay(draw, p, c, PIPE_OUT)
    fill(draw, m.start, "#ffff00")

    im.show()

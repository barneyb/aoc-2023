from PIL import Image, ImageDraw

from aoc2023.day16 import *
from util import aoc

PX = 1
PITCH = PX * 5
OBJECT = "#FF0000"


def fill(draw, p, color):
    x, y = p
    x *= PITCH
    y *= PITCH
    draw.rectangle((x, y, x + PITCH - 1, y + PITCH - 1), color)


def obj(draw, p, s):
    x, y = p
    x *= PITCH
    y *= PITCH
    match s:
        case "/":
            draw.line((x + PITCH - 1, y, x, y + PITCH - 1), OBJECT, PX)
        case "\\":
            draw.line((x + PITCH - 1, y + PITCH - 1, x, y), OBJECT, PX)
        case "|":
            draw.line((x + PITCH // 2, y, x + PITCH // 2, y + PITCH - 1), OBJECT, PX)
        case "-":
            draw.line((x, y + PITCH // 2, x + PITCH - 1, y + PITCH // 2), OBJECT, PX)


def to_color(n, mx):
    h = hex(128 + round(n / mx * 127))[2:].rjust(2, "0")
    return "#" + h * 3


if __name__ == "__main__":
    data = aoc.get_input(__file__)
    model = parse(data)
    w, h, layout = model
    hist = Counter()
    for cs in every_source(model):
        hist.update(cs.keys())
    max_e = max(hist.values())

    im = Image.new(mode="RGB", size=(w * PITCH, h * PITCH), color=0)
    draw = ImageDraw.Draw(im)

    for p in hist:
        e = hist[p]
        fill(draw, p, to_color(e, max_e))
    for p in layout:
        obj(draw, p, layout[p])

    im.show()

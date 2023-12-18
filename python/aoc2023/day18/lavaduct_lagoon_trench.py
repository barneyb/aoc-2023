from PIL import Image, ImageDraw

import aoc2023.day18 as lagoon
from util import aoc

PX = None
GROUND = "#333333"

if __name__ == "__main__":
    data = aoc.get_input(__file__)
    plan = lagoon.parse(data)
    lo, hi, trench = lagoon.cut_trench(plan)
    dx, dy = lo
    dx, dy = -dx, -dy
    width = hi[0] - lo[0] + 1
    height = hi[1] - lo[1] + 1

    im = Image.new(mode="RGB", size=(width, height), color=GROUND)
    draw = ImageDraw.Draw(im)
    prev = (dx, dy)
    for (x, y), c in trench.items():
        p = (x + dx, y + dy)
        draw.line((prev, p), c)
        prev = p
    im.show()

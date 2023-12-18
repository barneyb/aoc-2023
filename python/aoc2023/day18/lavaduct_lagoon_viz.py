from PIL import Image, ImageDraw

import aoc2023.day18 as ll
from util import aoc

PX = None
GROUND = "#333333"
LAGOON = "#FF8000"

if __name__ == "__main__":
    data = aoc.get_input(__file__)
    plan = ll.parse(data)
    trench = ll.cut_trench(plan)
    lo, hi = ll.bounds(trench)
    inside = ll.find_point_inside(lo, hi, trench)
    lagoon = ll.dig_out_lagoon(trench, inside)
    dx, dy = lo
    dx, dy = -dx, -dy
    width = hi[0] - lo[0] + 1
    height = hi[1] - lo[1] + 1

    im = Image.new(mode="RGB", size=(width, height), color=GROUND)
    draw = ImageDraw.Draw(im)
    for x, y in lagoon:
        x, y = x + dx, y + dy
        draw.rectangle((x, y, x, y), LAGOON)
    prev = (dx, dy)
    for (x, y), c in trench.items():
        p = (x + dx, y + dy)
        draw.line((prev, p), c)
        prev = p
    im.show()

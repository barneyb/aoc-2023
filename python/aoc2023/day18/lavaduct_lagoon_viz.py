from PIL import Image, ImageDraw

import aoc2023.day18 as ll
from util import aoc

PX = None
GROUND = "#333333"
LAGOON = "#FF8000"

if __name__ == "__main__":
    data = aoc.get_input(__file__)
    plan = ll.parse(data)
    plan = ll.reparse(plan)
    x, y = 0, 0
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    for d, n in plan:
        x, y = ll.move((x, y), d, n)
        x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, x), max(y2, y)
    lo, hi = (x1, y1), (x2, y2)
    dx, dy = lo
    dx, dy = -dx + 1, -dy + 1
    width = hi[0] - lo[0] + 1
    height = hi[1] - lo[1] + 1
    factor = 1000 / max(width, height)

    im = Image.new(
        mode="RGB",
        size=(round((width + 1) * factor), round((height + 1) * factor)),
        color=GROUND,
    )
    draw = ImageDraw.Draw(im)
    prev = (dx * factor, dy * factor)
    for d, n in plan:
        x, y = ll.move((x, y), d, n)
        p = ((x + dx) * factor, (y + dy) * factor)
        draw.line((prev, p), LAGOON)
        prev = p
    im.show()

from PIL import Image, ImageDraw

import aoc2023.day18 as ll
from aoc2023.day18.lavaduct_lagoon_test import EXAMPLE

PX = None
GROUND = "#333333"
LAGOON = "#FF8000"
TICK = "#999999"
RULE = "#CCCCCC"

if __name__ == "__main__":
    data = EXAMPLE
    # data = aoc.get_input(__file__)

    plan = ll.parse(data)

    plan = [(d, n) for d, n, _ in plan]
    # plan = ll.reparse(plan)

    lo, hi, corners = ll.get_bounds(plan)
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
    draw.line((prev, tuple(d + factor / 2 for d in prev)), TICK)
    for x, y in corners:
        p = ((x + dx) * factor, (y + dy) * factor)
        draw.line((prev, p), LAGOON)
        prev = p
    draw.line((prev, tuple(d + factor / 2 for d in prev)), TICK)
    if height < 20:
        # x axis
        for x in range(width):
            a = ((x + dx) * factor, 0)
            b = ((x + dx) * factor, factor / 2)
            draw.line((a, b), TICK)
        # y axis
        for y in range(height):
            a = (0, (y + dx) * factor)
            b = (factor / 2, (y + dx) * factor)
            draw.line((a, b), TICK)
    # rules
    for y, x1, x2 in ll.get_rules(corners):
        if x2 < x1:
            x2, x1 = x1, x2
        y = (y + dy) * factor
        x1 = (x1 + dx) * factor
        x2 = (x2 + dx) * factor
        draw.rectangle((x1, y - 2, x2, y + 2), outline=RULE)

    im.show()

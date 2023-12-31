from collections import Counter

from util import aoc, block_print


def parse(input, width=25, height=6):
    size = width * height
    layers = []
    layer = None
    row = None
    for i, c in enumerate(input):
        if i % width == 0:
            if i % size == 0:
                layer = []
                layers.append(layer)
            row = []
            layer.append(row)
        row.append(int(c))
    return layers


def part_one(layers):
    fewest_zeros = 999_999_999
    result = None
    for layer in layers:
        hist = Counter()
        for row in layer:
            for p in row:
                hist[p] += 1
        if hist[0] < fewest_zeros:
            fewest_zeros = hist[0]
            result = hist[1] * hist[2]
    return result


def part_two_raw(layers, bg=" ", fg="#"):
    width = len(layers[0][0])
    height = len(layers[0])
    image = []
    for y in range(height):
        if y > 0:
            image.append("\n")
        for x in range(width):
            for l in layers:
                match l[y][x]:
                    case 0:
                        image.append(bg)
                    case 1:
                        image.append(fg)
                    case 2:
                        continue
                break
    return "".join(image)


def part_two(layers):
    return block_print.read(part_two_raw(layers))


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

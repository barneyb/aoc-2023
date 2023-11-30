from util import aoc
from util.Histogram import Histogram


def parse(input, width=25, height=6):
    size = width * height
    layers = []
    layer = None
    row = None
    for i, c in enumerate(input):
        if i % size == 0:
            layer = []
            layers.append(layer)
        if i % width == 0:
            row = []
            layer.append(row)
        row.append(int(c))
    return layers


def part_one(layers):
    fewest_zeros = 999_999_999
    result = None
    for layer in layers:
        hist = Histogram()
        for row in layer:
            for d in row:
                hist.count(d)
        if hist[0] < fewest_zeros:
            fewest_zeros = hist[0]
            result = hist[1] * hist[2]
    return result


if __name__ == "__main__":
    aoc.solve(__file__,
              parse,
              part_one)

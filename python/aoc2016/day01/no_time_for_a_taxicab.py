from util import aoc


def parse(input):
    return [(s[0], int(s[1:])) for s in input.split(", ")]


def part_one(model):
    h = 0
    x = 0
    y = 0
    for (d, n) in model:
        if d == 'R':
            h += 1
        else:
            h -= 1
        match (h + 4) % 4:
            case 0:
                y -= n
            case 1:
                x += n
            case 2:
                y += n
            case 3:
                x -= n
    return abs(x) + abs(y)


def part_two(model):
    return None


if __name__ == "__main__":
    aoc.solve(__file__,
              parse,
              part_one,
              part_two)

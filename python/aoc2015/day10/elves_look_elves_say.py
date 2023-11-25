from util import aoc


def look_and_say(model):
    last = model[0]
    n = 1
    result = ""
    for c in model[1:]:
        if last == c:
            n += 1
        else:
            result += str(n) + last
            last = c
            n = 1
    return result + str(n) + last


def part_one(model):
    for _ in range(40):
        model = look_and_say(model)
    return len(model)


def part_two(model):
    for _ in range(50):
        model = look_and_say(model)
    return len(model)


if __name__ == "__main__":
    aoc.solve(__file__,
              None,
              part_one,
              part_two)

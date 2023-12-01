import re

from util import aoc


def part_one(input):
    re_first = re.compile(r"\D*(\d)")
    re_last = re.compile(r"(\d)\D*$")
    nums = []
    for line in input.splitlines():
        f = re_first.match(line)
        l = re_last.search(line)
        nums.append(f.group(1) + l.group(1))
    return sum(int(n) for n in nums)


def part_two(input):
    re_digit = re.compile(r"\d|one|two|three|four|five|six|seven|eight|nine")
    model = []
    for line in input.splitlines():
        digits = []
        i, l = 0, len(line)
        while i < l:
            m = re_digit.search(line, i)
            if not m:
                break
            digits.append(parse_digit(m.group()))
            i += 1
        model.append(digits[0] * 10 + digits[-1])
    return sum(model)


def parse_digit(s):
    if len(s) == 1:
        return int(s)
    match s:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
    raise RuntimeError(f"can't parse digit '{s}'")


if __name__ == "__main__":
    aoc.solve(__file__,
              None,
              part_one,
              part_two)  # not 55330

import re

from util import aoc


def part_one(input):
    return either_part(
        input,
        "1|2|3|4|5|6|7|8|9",
        int)


def either_part(input, digit_expr, parse_digit):
    re_first = re.compile(r"(" + digit_expr + ")")
    re_last = re.compile(r"(" + digit_expr[::-1] + ")")
    nums = []
    for line in input.splitlines():
        f = re_first.search(line).group()
        l = re_last.search(line[::-1]).group()[::-1]
        nums.append(parse_digit(f) * 10 + parse_digit(l))
    return sum(n for n in nums)


def part_two(input):
    return either_part(
        input,
        "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine",
        parse_word_digit)


def parse_word_digit(s):
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

import re

from util import aoc

NAMES = {"one"  : 1,
         "two"  : 2,
         "three": 3,
         "four" : 4,
         "five" : 5,
         "six"  : 6,
         "seven": 7,
         "eight": 8,
         "nine" : 9,
         }


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
    return NAMES[s]


if __name__ == "__main__":
    aoc.solve(__file__,
              None,
              part_one,
              part_two)  # not 55330

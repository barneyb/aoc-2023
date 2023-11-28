from util import aoc


def part_one(input):
    comp_len = len(input)
    decomp_len = 0
    pos = 0
    while pos < comp_len:
        open = input.find("(", pos)
        if open < 0:
            decomp_len += comp_len - pos
            break
        decomp_len += open - pos
        pos = open + 1
        x = input.find("x", pos)
        pos = x + 1
        close = input.find(")", pos)
        pos = close + 1
        l = int(input[(open + 1):x])
        pos += l
        n = int(input[(x + 1):close])
        decomp_len += l * n
    return decomp_len


if __name__ == "__main__":
    aoc.solve(__file__,
              None,
              part_one)

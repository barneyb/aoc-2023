from collections import Counter

from util import aoc


def parse_round(round):
    hist = Counter()
    for n, c in (c.strip().split(" ") for c in round.split(",")):
        hist[c] += int(n)
    return hist["red"], hist["green"], hist["blue"]


def parse_line(line):
    game, rounds = line.split(":")
    game = int(game.split(" ")[1])
    rounds = [parse_round(r) for r in rounds.split(";")]
    return game, rounds


def parse(input):
    return [parse_line(l) for l in input.splitlines()]


def part_one(games):
    sum = 0
    red, green, blue = 12, 13, 14
    for id, rounds in games:
        if all(r <= red and g <= green and b <= blue for r, g, b in rounds):
            sum += id
    return sum


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
    )

import operator
from functools import reduce

from util import aoc

OUTPUT = 10_000


def parse(input):
    # list of (value, bot) tuples
    inputs = []
    # map of bot -> (lo, hi) target tuples (+10K for outputs)
    rules = {}

    for words in (line.split(" ") for line in input.splitlines()):
        if len(words) == 6:
            # value 3 goes to bot 1
            # 0     1 2    3  4   5
            inputs.append((int(words[1]), int(words[5])))
        else:
            # bot 1 gives low to output 1 and high to bot 0
            # 0   1 2     3   4  5      6 7   8    9  10  11
            a = int(words[6])
            b = int(words[11])
            rules[int(words[1])] = (
                a if words[5] == "bot" else OUTPUT + a,
                b if words[10] == "bot" else OUTPUT + b,
            )

    return inputs, rules


def both_parts(model, lo=17, hi=61):
    who, outputs = simulate(model, lo, hi)
    return who, reduce(operator.mul, outputs[0:3], 1)


def simulate(model, lo, hi):
    """I run the simulation, returning a tuple with the bot number that compared
    the passed lo/hi values and a list of values in the outputs bins.
    """
    inputs, rules = model
    bot_values = {}
    outputs = {}
    who = None

    def accept(a, bot):
        nonlocal who
        if bot not in bot_values:
            bot_values[bot] = a
            return
        b = bot_values[bot]
        del bot_values[bot]
        if a > b:
            a, b = b, a
        if a == lo and b == hi:
            who = bot
        for n, t in zip((a, b), rules[bot]):
            if t < OUTPUT:
                accept(n, t)
            else:
                outputs[t - OUTPUT] = n

    for val, to in inputs:
        accept(val, to)

    # implicit assertion: outputs are numbered from zero, with no jumps
    return who, [outputs[i] for i in range(len(outputs))]


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        both_parts,
    )

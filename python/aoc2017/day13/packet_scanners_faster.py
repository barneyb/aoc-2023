"""I am a reimplementation of part two's solution to do some of the arithmetic
earlier and reuse the results, instead of recomputing. It cuts the runtime down
by about 1/6 (~1.5s to ~1.25s) on my machine. It's also quite a bit more
difficult to read and understand.
"""
import itertools

from aoc2017.day13.packet_scanners import parse, part_one
from util import aoc


def get_cycles(ranges):
    """I return a set of two-tuples representing the firewall layer ranges. Each
    tuple has the length of the layer's cycle and the number of layers skipped
    (non-layer depths) since the last layer.
    """
    cycles = []
    skips = 0
    for rng in ranges:
        if rng is None:
            skips += 1
        else:
            cycles.append((rng + rng - 2, skips))
            skips = 0
    return cycles


def get_layers_caught(cycles, delay):
    """I iterate over the layers which will catch a packet sent with the passed
    delay. Note I accept a list of cycle tuples, not a list of ranges!
    """
    tick = delay
    for cycle, skips in cycles:
        tick += skips
        if tick % cycle == 0:
            yield tick - delay
        tick += 1


def part_two(ranges):
    cycles = get_cycles(ranges)
    for delay in itertools.count():
        try:
            next(get_layers_caught(cycles, delay))
        except StopIteration:
            # never got caught!
            return delay


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

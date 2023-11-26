from os import path
from re import split

from .perf import format_ns, timed_ns


def get_input(file):
    # This import checks the token file _during initialization_, so only import
    # when it's first used.
    from aocd import get_data

    parts = split("[^0-9]+", path.dirname(file))
    d = int(parts[len(parts) - 1])
    y = int(parts[len(parts) - 2])
    return get_data(year=y, day=d)


def solve(file, parse, *parts):
    (input, ns) = timed_ns(lambda: get_input(file))
    print(f"Read   ({format_ns(ns)}): {len(input)} chars")
    for i, part in enumerate(parts):
        if parse is None:
            model = input
        else:
            (model, ns) = timed_ns(lambda: parse(input))
            if i == 0 and model != input:
                print(f"Parse  ({format_ns(ns)})")
        (answer, ns) = timed_ns(lambda: part(model))
        print(f"Part {i + 1} ({format_ns(ns)}): {answer if answer else '-'}")

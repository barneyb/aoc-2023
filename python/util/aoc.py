from os import path
from re import split
from time import perf_counter_ns

NANOS_PER_MILLISECOND = 1_000_000

NANOS_PER_SEC = 1_000_000_000


def get_input(file):
    from aocd import get_data

    parts = split("[^0-9]+", path.dirname(file))
    d = int(parts[len(parts) - 1])
    y = int(parts[len(parts) - 2])
    return get_data(year=y, day=d)


def timed_ns(work):
    start = perf_counter_ns()
    result = work()
    end = perf_counter_ns()
    return result, end - start


def solve(file, parse, *parts):
    (input, ns) = timed_ns(lambda: get_input(file))
    print(f"Read   ({duration_ns(ns)}): {len(input)} chars")
    for i, part in enumerate(parts):
        if parse is None:
            model = input
        else:
            (model, ns) = timed_ns(lambda: parse(input))
            if i == 0:
                print(f"Parse  ({duration_ns(ns)})")
        (answer, ns) = timed_ns(lambda: part(model))
        print(f"Part {i + 1} ({duration_ns(ns)}): {answer if answer else '-'}")


def duration_ns(nanos):
    if nanos > NANOS_PER_SEC:
        return f"{nanos / NANOS_PER_SEC :>7,.2f} sec"
    return f"{nanos / NANOS_PER_MILLISECOND :>8,.2f} ms"

from re import split
from time import perf_counter_ns


def get_input(file):
    from aocd import get_data

    parts = split("[^0-9]+", file)
    d = int(parts[len(parts) - 2])
    y = int(parts[len(parts) - 3])
    return get_data(year=y, day=d)


def timed_ns(work):
    start = perf_counter_ns()
    result = work()
    end = perf_counter_ns()
    return result, end - start


def solve(file, parse, *parts):
    (input, ns) = timed_ns(lambda: get_input(file))
    print(f"Read   ({duration_ns(ns)}): {len(input)} chars")
    if parse is None:
        model = input
    else:
        (model, ns) = timed_ns(lambda: parse(input))
        print(f"Parse  ({duration_ns(ns)})")
    i = 0
    for part in parts:
        i += 1
        (answer, ns) = timed_ns(lambda: part(model))
        print(f"Part {i} ({duration_ns(ns)}): {answer if answer else '-'}")


def duration_ns(nanos):
    # 1 million nanoseconds per millisecond
    return f"{nanos / 1_000_000:>8,.2f} ms"

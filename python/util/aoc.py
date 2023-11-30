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
    (input, read_ns) = timed_ns(lambda: get_input(file))
    print(f"Read   ({format_ns(read_ns)}) : {len(input)} chars")
    print("--------------------")
    total_ns = 0
    i = 0
    for part in parts:
        if parse is None:
            model = input
        else:
            (model, ns) = timed_ns(lambda: parse(input))
            total_ns += ns
            if i == 0 and model != input:
                print(f"Parse  ({format_ns(ns)})")
        (answers, ns) = timed_ns(lambda: part(model))
        total_ns += ns
        if type(answers) != tuple:
            answers = (answers,)
        for a in answers:
            i += 1
            timing = f"({format_ns(ns)})" if ns > 0 else " " * 13
            print(f"Part {i} {timing} : {'-' if a is None else a}")
            ns = 0
    print(f"Total  ({format_ns(total_ns)})")
    print("--------------------")
    print(f"Grand  ({format_ns(total_ns + read_ns)})")

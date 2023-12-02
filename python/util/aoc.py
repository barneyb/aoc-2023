from os import path
from re import split

from .timing import format_ns, with_ns
from .tracing import format_alloc, with_alloc

BLOCK = "█"


def get_input(file):
    # This import checks the token file _during initialization_, so only import
    # when it's first used.
    from aocd import get_data

    parts = split("[^0-9]+", path.dirname(file))
    d = int(parts[len(parts) - 1])
    y = int(parts[len(parts) - 2])
    return get_data(year=y, day=d)


def __with_metric(file, run_with_metric, format_metric, parse, *parts):
    (input, read_m) = run_with_metric(lambda: get_input(file))
    print(f"Read    ({format_metric(read_m)}) : {len(input)} chars")
    print("-" * 21)
    total_m = 0
    i = 1
    for part in parts:
        if parse is None:
            model = input
        else:
            (model, m) = run_with_metric(lambda: parse(input))
            total_m += m
            if i == 1 and model != input:
                print(f"Parse   ({format_metric(m)})")
        (answers, m) = run_with_metric(lambda: part(model))
        total_m += m
        if type(answers) != tuple:
            answers = (answers,)
        c = ord("a")
        for a in answers:
            metric = f"({format_metric(m)})" if m > 0 else " " * 13
            if type(a) == str and "\n" in a and a[0] != "\n":
                a = "\n" + a
            lbl = f"{i} " if len(answers) == 1 else f"{i}{chr(c)}"
            print(f"Part {lbl} {metric} : {'-' if a is None else a}")
            m = 0
            c += 1
        i += 1
    print(f"Total   ({format_metric(total_m)})")
    print("-" * 21)
    print(f"Grand   ({format_metric(total_m + read_m)})")


def solve(file, parse, *parts):
    __with_metric(file, with_ns, format_ns, parse, *parts)


def trace(file, parse, *parts):
    __with_metric(file, with_alloc, format_alloc, parse, *parts)

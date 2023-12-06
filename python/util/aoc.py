import importlib
from os import path
from re import split

from .timing import format_ns, with_bench, with_ns
from .tracing import format_alloc, with_alloc

BLOCK = "█"


def entry_point(year, day, data):
    mod_name = f"aoc{year}.day{day:02}"
    mod = importlib.import_module(mod_name)
    mod_attrs = dir(mod)
    parse = lambda d: d
    if "parse" in mod_attrs:
        parse = mod.parse
    if "both_parts" in mod_attrs:
        a, b = mod.both_parts(parse(data))
    else:
        a = mod.part_one(parse(data))
        b = None
        if "part_two" in mod_attrs:
            b = mod.part_two(parse(data))
    return a, b


def get_input(file):
    # This import checks the token file _during initialization_, so only import
    # when it's first used.
    from aocd import get_data

    parts = split("[^0-9]+", path.dirname(file))
    d = int(parts[len(parts) - 1])
    y = int(parts[len(parts) - 2])
    return get_data(year=y, day=d)


def _with_metric(file, run_with_metric, format_metric, parse, *parts):
    read_with_metric = run_with_metric
    if type(run_with_metric) == tuple:
        read_with_metric, run_with_metric = run_with_metric
    (input, read_m) = read_with_metric(lambda: get_input(file))
    filename = file.split("/")[-1].split(".")[0]
    bar_len = max(len(filename) + 5, 21)
    print(f"Read    ({format_metric(read_m)}) : {len(input)} chars")
    print(f"- {filename.replace('_', ' ')} " + ("-" * (bar_len - len(filename) - 3)))
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
    print("-" * bar_len)
    print(f"Grand   ({format_metric(total_m + read_m)})")


def solve(file, parse, *parts):
    _with_metric(file, with_ns, format_ns, parse, *parts)


def bench(file, parse, *parts):
    _with_metric(file, (with_ns, with_bench), format_ns, parse, *parts)


def trace(file, parse, *parts):
    _with_metric(file, with_alloc, format_alloc, parse, *parts)

import glob
import importlib
import importlib.util
import os

from util.aoc import entry_point


def is_supported(y, d):
    mod = importlib.import_module(f"aoc{y}.day{d:02}")
    mod_attrs = dir(mod)
    return "part_one" in mod_attrs or "both_parts" in mod_attrs


def support():
    search_pattern = os.path.join("..", "aoc*", "day*", "__init__.py")
    files = glob.glob(
        search_pattern,
        root_dir=os.path.dirname(__file__),
        recursive=True,
    )
    pairs = [(int(y[3:]), int(d[3:])) for y, d in [f.split("/")[1:3] for f in files]]
    return [(y, d) for y, d in pairs if is_supported(y, d)]


def solve(year, day, data):
    return entry_point(year, day, data)

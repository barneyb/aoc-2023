from .pulse_propagation import *

EXAMPLE_A = """\
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

MODEL_A = {
    "broadcaster": (">", ["a", "b", "c"], None),
    "a": ("%", ["b"], Switch()),
    "b": ("%", ["c"], Switch()),
    "c": ("%", ["inv"], Switch()),
    "inv": ("&", ["a"], {"c": False}),
}

EXAMPLE_B = """\
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

MODEL_B = {
    "broadcaster": (">", ["a"], None),
    "a": ("%", ["inv", "con"], Switch()),
    "inv": ("&", ["b"], {"a": False}),
    "b": ("%", ["con"], Switch()),
    "con": ("&", ["output"], {"a": False, "b": False}),
}


def test_parse():
    assert parse(EXAMPLE_A) == MODEL_A
    assert parse(EXAMPLE_B) == MODEL_B


def test_part_one_a():
    assert part_one(MODEL_A) == 32000000


def test_part_one_b():
    assert part_one(MODEL_B) == 11687500

from .snowverload import *

EXAMPLE = """\
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""
MODEL = [
    ("jqt", "rhn"),
    ("jqt", "xhk"),
    ("jqt", "nvd"),
    ("rsh", "frs"),
    ("rsh", "pzl"),
    ("rsh", "lsr"),
    ("xhk", "hfx"),
    ("cmg", "qnr"),
    ("cmg", "nvd"),
    ("cmg", "lhk"),
    ("cmg", "bvb"),
    ("rhn", "xhk"),
    ("rhn", "bvb"),
    ("rhn", "hfx"),
    ("bvb", "xhk"),
    ("bvb", "hfx"),
    ("pzl", "lsr"),
    ("pzl", "hfx"),
    ("pzl", "nvd"),
    ("qnr", "nvd"),
    ("ntq", "jqt"),
    ("ntq", "hfx"),
    ("ntq", "bvb"),
    ("ntq", "xhk"),
    ("nvd", "lhk"),
    ("lsr", "lhk"),
    ("rzs", "qnr"),
    ("rzs", "cmg"),
    ("rzs", "lsr"),
    ("rzs", "rsh"),
    ("frs", "qnr"),
    ("frs", "lhk"),
    ("frs", "lsr"),
]


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_part_one():
    ans = part_one(MODEL)
    print(ans)
    assert ans[0] == 54

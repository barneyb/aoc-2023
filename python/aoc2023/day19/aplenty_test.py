from .aplenty import *

EXAMPLE = """\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""
MODEL = parse(EXAMPLE)


def test_parse_workflow():
    assert parse_workflow("px{a<2006:qkq,m>2090:A,rfg}") == (
        "px",
        [
            ("a", "<", 2006, "qkq"),
            ("m", "≥", 2091, "A"),
        ],
        "rfg",
    )


def test_parse_part():
    assert parse_part("{x=787,m=2655,a=1222,s=2876}") == {
        "x": 787,
        "m": 2655,
        "a": 1222,
        "s": 2876,
    }


def test_evaluate():
    assert evaluate(MODEL[0]["in"], MODEL[1][0]) == "qqz"
    assert evaluate(MODEL[0]["in"], MODEL[1][1]) == "px"


def test_accept():
    assert accept(MODEL[0], MODEL[1][0])
    assert not accept(MODEL[0], MODEL[1][1])
    assert accept(MODEL[0], MODEL[1][2])
    assert not accept(MODEL[0], MODEL[1][3])
    assert accept(MODEL[0], MODEL[1][4])


def test_part_one():
    assert part_one(MODEL) == 19114


def test_eval_many():
    def check(ps, expected):
        assert list(eval_many(workflow, ps)) == expected

    workflow = [("a", "≥", 6, "hit")], "thru"
    check({"a": (1, 5)}, [("thru", {"a": (1, 5)})])
    check({"a": (1, 6)}, [("thru", {"a": (1, 6)})])
    check({"a": (1, 7)}, [("hit", {"a": (6, 7)}), ("thru", {"a": (1, 6)})])
    check({"a": (4, 9)}, [("hit", {"a": (6, 9)}), ("thru", {"a": (4, 6)})])
    check({"a": (5, 9)}, [("hit", {"a": (6, 9)}), ("thru", {"a": (5, 6)})])
    check({"a": (6, 9)}, [("hit", {"a": (6, 9)})])

    workflow = [("a", "<", 5, "hit")], "thru"
    check({"a": (1, 5)}, [("hit", {"a": (1, 5)})])
    check({"a": (1, 6)}, [("hit", {"a": (1, 5)}), ("thru", {"a": (5, 6)})])
    check({"a": (4, 9)}, [("hit", {"a": (4, 5)}), ("thru", {"a": (5, 9)})])
    check({"a": (5, 9)}, [("thru", {"a": (5, 9)})])
    check({"a": (6, 9)}, [("thru", {"a": (6, 9)})])


def test_count_parts():
    assert count_parts({"x": (0, 1), "y": (0, 1)}) == 1
    assert count_parts({"x": (0, 1), "y": (0, 5)}) == 5
    assert count_parts({"x": (0, 5), "y": (0, 1)}) == 5
    assert count_parts({"x": (5, 10), "y": (3, 6)}) == 15


def test_part_two():
    assert part_two(MODEL) == 167409079868000

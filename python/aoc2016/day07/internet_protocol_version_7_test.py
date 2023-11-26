from internet_protocol_version_7 import *


def test_parse_addr():
    other, hyper = parse_addr("abba[mnop]qrst")
    assert other == ["abba", "qrst"]
    assert hyper == ["mnop"]


def test_parse():
    assert parse("""a[b]c
    d[e]f[g]h""") == [
        (["a", "c"], ["b"]),
        (["d", "f", "h"], ["e", "g"])
    ]


def test_has_abba():
    assert has_abba(["abba", "qrst"])
    assert not has_abba(["mnop"])
    # have to be different letters
    assert not has_abba(["aaaa"])

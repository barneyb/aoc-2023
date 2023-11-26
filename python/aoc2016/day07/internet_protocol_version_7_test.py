from internet_protocol_version_7 import *


def test_parse_addr():
    super, hyper = parse_addr("abba[mnop]qrst")
    assert super == ["abba", "qrst"]
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


def test_supports_tls():
    assert supports_tls(parse_addr("abba[mnop]qrst"))
    assert not supports_tls(parse_addr("abcd[bddb]xyyx"))
    assert not supports_tls(parse_addr("aaaa[qwer]tyui"))
    assert supports_tls(parse_addr("ioxxoj[asdfgh]zxcvbn"))


def test_has_aba():
    assert list(get_abas(["aba", "xyz"])) == ["aba"]
    assert list(get_abas(["zazbz", "cdb"])) == ["zaz", 'zbz']


def test_supports_ssl():
    assert supports_ssl(parse_addr("aba[bab]xyz"))
    assert not supports_ssl(parse_addr("xyx[xyx]xyx"))
    assert supports_ssl(parse_addr("aaa[kek]eke"))
    assert supports_ssl(parse_addr("zazbz[bzb]cdb"))

from .perf import *


def test_timed_ns():
    (r, ns) = timed_ns(lambda: 42)
    assert r == 42
    # this is sort of a BS assertion, but it takes over a millisecond to return
    # a number from a lambda, it's not really a false positive. :)
    assert 0 <= ns <= NANOS_PER_MILLISECOND


def test_format_ns():
    def fmt(ns):
        r = format_ns(ns)
        assert len(r) == 11
        return r.strip()

    assert fmt(0) == "0.00 ms"
    assert fmt(1) == "0.00 ms"
    assert fmt(1_000) == "0.00 ms"
    assert fmt(10_000) == "0.01 ms"
    assert fmt(1_234_567) == "1.23 ms"
    assert fmt(123_456_789) == "123.46 ms"
    assert fmt(1_234_567_890) == "1.23 sec"

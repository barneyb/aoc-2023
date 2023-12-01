from util.Histogram import Histogram


def test_len():
    h = Histogram()
    assert len(h) == 0
    h.count(42)
    assert len(h) == 1
    h.count(42)
    assert len(h) == 1


def test_count():
    h = Histogram()
    h.count(1)
    h.count(2)
    h.count(2)
    h.count(3, 3)
    assert h[1] == 1
    assert h[2] == 2
    assert h[3] == 3


def test_missing_bucket_is_zero():
    h = Histogram()
    h.count(1)
    assert h[1] == 1
    assert h[2] == 0  # not an error!
    assert list(h.keys()) == [1]
    assert list(h.values()) == [1]
    assert list(h.items()) == [(1, 1)]

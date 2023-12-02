from .tracing import format_alloc


def test_format_alloc():
    def fmt(ns):
        r = format_alloc(ns)
        assert len(r) == 11
        return r.strip()

    assert fmt(0) == "0 B"
    assert fmt(1023) == "1023 B"
    assert fmt(1024) == "1024 B"
    assert fmt(1025) == "1.00 KB"
    assert fmt(1024 * 1024 + 1) == "1.0 MB"

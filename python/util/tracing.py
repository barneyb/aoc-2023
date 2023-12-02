import tracemalloc

BYTES_PER_KB = 1024
BYTES_PER_MB = 1024 * BYTES_PER_KB


def with_alloc(work):
    """I execute the passed work and return a tuple containing the result and
    the number of bytes it allocated.
    """
    tracemalloc.start()
    result = work()
    snap = tracemalloc.take_snapshot()
    tracemalloc.stop()
    return result, sum(s.size for s in snap.statistics("filename"))


def format_alloc(alloc):
    """I format the passed byte count. The result will always be 11 characters
    long, including the units.
    """
    if alloc > BYTES_PER_MB:
        return f"{alloc / BYTES_PER_MB:>8,.1f} MB"
    if alloc > BYTES_PER_KB:
        return f"{alloc / BYTES_PER_KB:>8,.2f} KB"
    return f"{alloc:>9d} B"

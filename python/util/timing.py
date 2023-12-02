import timeit
from time import perf_counter_ns

NANOS_PER_MILLISECOND = 1_000_000

NANOS_PER_SEC = 1_000_000_000


def with_ns(work):
    """I execute the passed work and return a tuple containing the result and
    the number of nanoseconds it took to execute.
    """
    start = perf_counter_ns()
    result = work()
    end = perf_counter_ns()
    return result, end - start


def with_bench(work):
    """I execute the passed work many times and return a tuple containing the
    result and the average number of nanoseconds it took to execute. The exact
    count will be determined based on its runtime, aiming to take no longer than
    a few seconds for the whole benchmark.
    """
    result, basis = with_ns(work)
    # at least three times, hopefully <3 seconds
    itrs = max(3, NANOS_PER_SEC // basis)
    sec = timeit.timeit(work, number=itrs)
    nanos = int(sec * NANOS_PER_SEC)
    return result, nanos // itrs


def format_ns(nanos):
    """I format the passed nanosecond as a duration. The result will always be
    11 characters long, including the units.
    """
    if nanos > NANOS_PER_SEC:
        return f"{nanos / NANOS_PER_SEC :>7,.2f} sec"
    if nanos > NANOS_PER_MILLISECOND:
        return f"{nanos / NANOS_PER_MILLISECOND :>8,.2f} ms"
    return f"{nanos:8,d} ns"

from time import perf_counter_ns

NANOS_PER_MILLISECOND = 1_000_000

NANOS_PER_SEC = 1_000_000_000


def timed_ns(work):
    """I execute the passed work and return a tuple containing the result and
    the number of nanoseconds it took to execute.
    """
    start = perf_counter_ns()
    result = work()
    end = perf_counter_ns()
    return result, end - start


def format_ns(nanos):
    """I format the passed nanosecond as a duration. The result will always be
    11 characters long, including the units.
    """
    if nanos > NANOS_PER_SEC:
        return f"{nanos / NANOS_PER_SEC :>7,.2f} sec"
    return f"{nanos / NANOS_PER_MILLISECOND :>8,.2f} ms"

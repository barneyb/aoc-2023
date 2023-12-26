import functools

N = 17
# fib(17) =  1597 iteratively
# fib(17) =  1597 naively
# fib(17) = (1597, 5167) in 5167 naive calls
# fib(17) = (1597, 5167) in   18 @cache calls
# fib(17) = (1597, 5167) in   18 memoized calls (15 memo hits)


###
# Elementary iterative impl.
###
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(f"fib({N}) =  {fib(N)} iteratively")


###
# Naive recursive impl.
###
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


print(f"fib({N}) =  {fib(N)} naively")


###
# Naive recursive impl, returning a 2-tuple of the Fibonacci number and the
# count of calls made. I.e., same algorithm as above, just with instrumentation.
###
def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n, 1
    else:
        a, c1 = fib(n - 2)
        b, c2 = fib(n - 1)
        return a + b, 1 + c1 + c2


calls = 0
print(f"fib({N}) = {fib(N)} in {calls:4} naive calls")


###
# using @functools.cache to memoize the same instrumented behavior.
###
@functools.cache
def fib_cache(n):
    global calls
    calls += 1
    if n < 2:
        return n, 1
    else:
        a, c1 = fib_cache(n - 2)
        b, c2 = fib_cache(n - 1)
        return a + b, 1 + c1 + c2


calls = 0
print(f"fib({N}) = {fib_cache(N)} in {calls:4} @cache calls")


###
# custom memoization higher-order function/decorator applied to the naive
# recursive impl. This is exactly equivalent to @functools.cache, though not as
# robust. E.g., it doesn't handle keyword args.
###
def memoize(func):
    def memoized(*args):
        global calls, memo_hits
        args = tuple(args)
        if args in memo:
            memo_hits += 1
        else:
            calls += 1
            memo[args] = func(*args)
        return memo[args]

    memo = {}
    return memoized


def fib(n):  # the non-instrumented naive implementation
    return n if n < 2 else fib(n - 2) + fib(n - 1)


fib = memoize(fib)  # apply the higher-order function, replacing the naive impl
calls = 0
memo_hits = 0
print(f"fib({N}) =  {fib(N)} in {calls:4} memoized calls (plus {memo_hits} memo hits)")


###
# Reuse the custom memoize function via the decorator syntax, instead of an
# invocation. Rather more concise, and prevents accidental non-memoized use,
# because it's part of the definition of 'fib'.
###
@memoize  # use decorator syntax (which looks like a Java annotation, but isn't)
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


calls = 0
memo_hits = 0
print(f"fib({N}) =  {fib(N)} in {calls:4} memoized calls (plus {memo_hits} memo hits)")

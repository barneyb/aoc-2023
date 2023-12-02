from util import aoc


def parse(input: str):
    lines = input.splitlines()
    initial_state = lines[0].split(":")[1].strip()
    notes = set()
    for l in lines[2:]:
        if l.endswith("#"):
            notes.add(l[0:5])
    return initial_state, notes


def part_one(model):
    # first element of generator comprehension over run_a_bit w/ gen=20
    return next(score for gen, score in run_a_bit(model) if gen == 20)


def run_a_bit(model):
    """Given a model, generate successive states as (gen, score) tuples. Gen is
    one-indexed.
    """
    state, notes = model
    offset = 0
    gen = 0
    while True:
        gen += 1
        next = ""
        window = "...."
        offset -= 2
        for c in state + "....":
            window += c
            next += "#" if window in notes else "."
            window = window[1:]
        offset += next.find("#")
        state = next.strip(".")
        score = sum(i + offset if c == "#" else 0 for i, c in enumerate(state))
        yield gen, score


def part_two(model):
    a, b, c = 0, 0, 0
    prev_score = 0
    for gen, score in run_a_bit(model):
        delta, prev_score = score - prev_score, score
        # four in a row past gen 100 means we're stable
        if gen > 100 and delta == a == b == c:
            return score + (50_000_000_000 - gen) * delta
        a, b, c = b, c, delta


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

import math
from collections import deque

from util import aoc


class Switch:
    """A boxed boolean"""

    def __init__(self, value=False):
        self.value = value

    def __bool__(self):
        return self.value

    def flip(self):
        self.value = not self.value

    def __eq__(self, other):
        return type(other) == Switch and self.value == other.value

    def __repr__(self):
        return f"Switch({repr(self.value)})"


def parse_module(line):
    name, recs = line.split(" -> ")
    recs = recs.split(", ")
    if name == "broadcaster":
        return name, (">", recs, None)
    t = name[0]
    name = name[1:]
    if t == "%":
        return name, (t, recs, Switch())
    else:  # &
        return name, (t, recs, {})


def parse(input):
    modules = [parse_module(l) for l in input.splitlines()]
    conjunctions = dict([(n, state) for n, (t, _, state) in modules if t == "&"])
    for n, (_, recs, _) in modules:
        for r in recs:
            if r in conjunctions:
                conjunctions[r][n] = False
    return dict(modules)


def push_button(modules, keep_going):
    pulses = deque()
    pulses.append(("button", False, "broadcaster"))  # PRESS!
    while pulses:
        src, val, dest = pulses.popleft()
        if not keep_going(src, val, dest):
            continue
        t, rs, state = modules[dest]
        match t:
            case "%":
                if val:
                    continue
                state.flip()
                val = bool(state)
            case "&":
                state[src] = val
                val = not all(state.values())
        for r in rs:
            pulses.append((dest, val, r))


def part_one(modules):
    def keep_going(src, val, dest):
        nonlocal hi, lo
        if val:
            hi += 1
        else:
            lo += 1
        return dest in modules  # not a sink

    hi, lo = 0, 0
    for _ in range(1000):
        push_button(modules, keep_going)
    return lo * hi


def graph_viz(modules):
    print("digraph {")
    print(f"  {'{'} rank=source; broadcaster; _ff; _c {'}'}")
    for n, (t, _, _) in sorted(modules.items()):
        if n == "broadcaster":
            print(f"  broadcaster [color=red, shape=box]")
            print(f"  rx [color=red, shape=box]")
            print(
                f'  _ff [label="flip-flop", shape=diamond, color=green, fontcolor=green]'
            )
            print(
                f'  _c [label="conjunction", shape=house, color=green, fontcolor=green]'
            )
        else:
            print(f"  {n} [shape={'diamond' if t == '%' else 'house'}]")
    for n, (t, rs, _) in modules.items():
        for r in rs:
            print(f"  {n} -> {r}")
    print("}")


def part_two(modules):
    def keep_going(src, val, dest):
        if dest in goal_modules and not val:
            goal_modules[dest] = press_count + 1
        return src != final_and

    # the conjunction leading into RX
    final_and = [n for n, (t, rs, _) in modules.items() if "rx" in rs]
    assert len(final_and) == 1, "found multiple inputs for 'rx'"
    final_and = final_and[0]
    # the ends of the four lobes leading into the final AND
    goal_modules = {n: 0 for n, (t, rs, _) in modules.items() if final_and in rs}
    for press_count in range(2**12):
        push_button(modules, keep_going)
    return math.lcm(*goal_modules.values())


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

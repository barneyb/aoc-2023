import math
from collections import Counter, defaultdict, namedtuple

from util import aoc


class Garden:
    def __init__(self, input):
        lines = input.splitlines()
        self.width = len(lines[0])
        self.height = len(lines)
        self.rocks = set()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "S":
                    self.start = (x, y)
                elif c == "#":
                    self.rocks.add((x, y))

    def neighbors(self, p):
        x, y = p
        return [
            p
            for p in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
            if p not in self.rocks
        ]

    def __str__(self):
        sb = []
        for y in range(self.height):
            for x in range(self.width):
                p = (x, y)
                sb.append("#" if p in self.rocks else "S" if p == self.start else ".")
            sb.append("\n")
        return "".join(sb)

    def __repr__(self):
        return "Garden('" + str(self) + "')"


def part_one(garden, total_steps=64):
    locs = set()
    locs.add(garden.start)
    for _ in range(total_steps):
        prev = locs
        locs = set()
        for p in prev:
            locs.update(garden.neighbors(p))
    return len(locs)


def naive_answer(locs_by_garden, mx=-math.inf, my=-math.inf):
    return sum(len(ls) for (x, y), ls in locs_by_garden.items() if x >= mx and y >= my)


def print_maps(step, locs_by_garden, extractors_by_name):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    for x, y in locs_by_garden:
        # x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, x), max(y2, y)
    x1 = 1

    # noinspection PyUnboundLocalVariable
    sb = [
        f"after {step} steps: {sum(1 for (x,y) in locs_by_garden if x >=x1 and y>=y1)} gardens w/ {naive_answer(locs_by_garden,x1,y1)} positions\n "
    ]
    for _ in extractors_by_name:
        for x in range(x1, x2 + 1):
            sb.append(f"{'│' if x == 0 else '':>5}")
        sb.append(f"{'':>5}")
    for y in range(y1, y2 + 1):
        sb.append("\n")
        for ex in extractors_by_name.values():
            sb.append("─" if y == 0 else " ")
            for x in range(x1, x2 + 1):
                sb.append(f"{ex((x, y)):>5}")
            sb.append("    ")
        sb.append(f"{'─' if y == 0 else '':>5}")
    sb.append("\n ")
    for _ in extractors_by_name:
        for x in range(x1, x2 + 1):
            sb.append(f"{'│' if x == 0 else '':>5}")
        sb.append(f"{'':>5}")
    sb.append("\n ")
    for n in extractors_by_name:
        sb.append(n.center((x2 - x1 + 1) * 5))
        sb.append(f"{'':>5}")
    print("".join(sb))


State = namedtuple("State", ["step", "trace_idx"])
FlipFlop = namedtuple("FlipFlop", ["len", "a", "b"])


def part_two(garden, total_steps=26_501_365):
    def do_step(curr):
        result = defaultdict(set)
        for gx, gy in curr:
            for p in curr[gx, gy]:
                for nx, ny in garden.neighbors(p):
                    if nx < 0:
                        result[gx - 1, gy].add((nx + garden.width, ny))
                    elif nx >= garden.width:
                        result[gx + 1, gy].add((nx - garden.width, ny))
                    elif ny < 0:
                        result[gx, gy - 1].add((nx, ny + garden.height))
                    elif ny >= garden.height:
                        result[gx, gy + 1].add((nx, ny - garden.height))
                    else:
                        result[gx, gy].add((nx, ny))
        # todo: can we cull anything more than a step away from an axis?
        return result

    def cycling(g):
        if g not in state_by_garden:
            return ""
        reached, idx = state_by_garden[g]
        if not flip_flops[idx]:
            return ""
        l, _, _ = flip_flops[idx]
        return "" if step <= reached + l else "+" if (step - reached) % 2 else "-"

    extractors = {
        "cnt": lambda g: len(locs_by_garden[g]) if g in locs_by_garden else "",
        "type": lambda g: state_by_garden[g].trace_idx if g in state_by_garden else "",
        "turn": lambda g: state_by_garden[g].step if g in state_by_garden else "",
        "cyc": cycling,
    }
    prev = {}
    locs_by_garden = defaultdict(set)
    locs_by_garden[0, 0].add(garden.start)
    # locations progressions, indexed by start_traces
    traces = []
    # cycle info, indexed by start_traces
    flip_flops = []
    # trace index by start location(s)
    start_traces = {}
    # trace index by garden coords of the tracked garden
    tracking_garden_traces = {}
    # starting step and trace index for each garden
    state_by_garden = {}
    found = Counter()
    for step in range(total_steps):
        for g in locs_by_garden:
            if g in prev:
                continue
            start = frozenset(locs_by_garden[g])
            if start in start_traces:
                idx = start_traces[start]
            else:
                idx = len(traces)
                traces.append([len(locs_by_garden[g])])
                flip_flops.append(None)
                start_traces[start] = idx
                tracking_garden_traces[g] = idx
            state_by_garden[g] = State(step, idx)
        if step and step % garden.width == total_steps % garden.width:
            if flip_flops and all(flip_flops) and cycling((1, 1)):
                edge = max(x for x, _ in locs_by_garden)
                cycle_len = (
                    state_by_garden[edge, 0].step - state_by_garden[edge - 1, 0].step
                )
                print(f"{total_steps - step} steps remain w/ {cycle_len} per cycle")
                remaining_cycles = (total_steps - step) // cycle_len
                print(
                    f"{remaining_cycles} cycles remain ({(total_steps - step) % cycle_len} off)"
                )
                predict = naive_answer(locs_by_garden, 1, 0)
                predict2 = predict
                seam_axis = max(x for x in range(edge, 0, -1) if cycling((x, 0)))
                print(f"axis: {seam_axis}")
                idx = state_by_garden[seam_axis, 0].trace_idx
                ff = flip_flops[idx]
                n = len(locs_by_garden[seam_axis, 0])
                print(f"  add an inverted {n} ({idx}: {ff})")
                predict += ff.a if ff.b == n else ff.b
                predict2 += ff.a + ff.b
                seam_quad = max(x for x in range(edge, 0, -1) if cycling((x, 1)))
                print(f"quad: {seam_quad}")
                idx = state_by_garden[seam_quad, 1].trace_idx
                ff = flip_flops[idx]
                n = len(locs_by_garden[seam_quad, 1])
                print(f"  add {seam_quad+1} inverted {n} ({idx}: {ff})")
                predict += (seam_quad + 1) * (ff.a if ff.b == n else ff.b)
                predict2 += (seam_quad + 1) * (ff.a if ff.b == n else ff.b)
                predict2 += (seam_quad + 2) * (ff.a if ff.a == n else ff.b)
                for x in range(seam_quad, edge):
                    g = (x + 1, 1)
                    if locs_by_garden[g]:
                        n = len(locs_by_garden[g])
                        print(f"  add a {n}")
                        predict += n
                        predict2 += 2 * n
                print(f"predict {predict} at {step+cycle_len}")
                print(f"predict {predict2} at {step+cycle_len*2}")

                # todo: once the four quadrants are computed, add the center/starting garden!
                found[remaining_cycles % 2] += 1
                print_maps(step, locs_by_garden, extractors)
                # if all(n > 1 for n in found.values()):
                #     return -1
        prev = locs_by_garden
        locs_by_garden = do_step(prev)
        for g in tracking_garden_traces:
            idx = tracking_garden_traces[g]
            if flip_flops[idx]:
                continue
            trace = traces[idx]
            trace.append(len(locs_by_garden[g]))
            if trace[-2:] == trace[-4:-2]:
                flip_flops[idx] = FlipFlop(len(trace) - 2, trace[-1], trace[-2])
            del trace
    print_maps(step + 1, locs_by_garden, extractors)

    # Didn't run far enough to establish a pattern to compute from, so just
    # count 'em up!
    return naive_answer(locs_by_garden)


if __name__ == "__main__":
    aoc.solve(
        __file__,
        Garden,
        part_one,
        part_two,
    )

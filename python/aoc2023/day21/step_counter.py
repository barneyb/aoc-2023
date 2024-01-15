from collections import defaultdict

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


def naive_answer(locs_by_garden):
    return sum(len(ls) for ls in locs_by_garden.values())


def print_maps(step, locs_by_garden, extractors_by_name):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    for x, y in locs_by_garden:
        x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, x), max(y2, y)

    # noinspection PyUnboundLocalVariable
    sb = [
        f"after {step} steps: {len(locs_by_garden)} gardens w/ {naive_answer(locs_by_garden)} positions\n "
    ]
    for _ in extractors_by_name:
        for x in range(x1, x2 + 1):
            sb.append(f"{'│' if x == 0 else '':>4}")
        sb.append("    ")
    for y in range(y1, y2 + 1):
        sb.append("\n")
        for ex in extractors_by_name.values():
            sb.append("─" if y == 0 else " ")
            for x in range(x1, x2 + 1):
                sb.append(f"{ex((x, y)):>4}")
            sb.append("   ")
        sb.append("─" if y == 0 else " ")
    sb.append("\n ")
    for _ in extractors_by_name:
        for x in range(x1, x2 + 1):
            sb.append(f"{'│' if x == 0 else '':>4}")
        sb.append("    ")
    sb.append("\n ")
    for n in extractors_by_name:
        sb.append(" ")
        sb.append(n.center((x2 - x1 + 1) * 4))
        sb.append("   ")
    print("".join(sb))


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
        return result

    extractors = {
        "cnt": lambda g: len(locs_by_garden[g]) if g in locs_by_garden else "",
        "type": lambda g: chr(ord("A") + state_by_garden[g][1])
        if g in state_by_garden
        else "",
        "turn": lambda g: state_by_garden[g][0] if g in state_by_garden else "",
        # "cyc": lambda g: "X"
        # if g in state_by_garden and flip_flops[state_by_garden[g][1]]
        # else "",
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
            state_by_garden[g] = (step, idx)
        print_maps(step, locs_by_garden, extractors)
        prev = locs_by_garden
        locs_by_garden = do_step(prev)
        for g in tracking_garden_traces:
            idx = tracking_garden_traces[g]
            if flip_flops[idx]:
                continue
            trace = traces[idx]
            trace.append(len(locs_by_garden[g]))
            if trace[-2:] == trace[-4:-2]:
                flip_flops[idx] = len(trace), trace[-1], trace[-2]
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

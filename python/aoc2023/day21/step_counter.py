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


def part_two(garden, total_steps=26_501_365):
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
        prev = locs_by_garden
        locs_by_garden = defaultdict(set)
        for gx, gy in prev:
            for p in prev[gx, gy]:
                for nx, ny in garden.neighbors(p):
                    if nx < 0:
                        locs_by_garden[gx - 1, gy].add((nx + garden.width, ny))
                    elif nx >= garden.width:
                        locs_by_garden[gx + 1, gy].add((nx - garden.width, ny))
                    elif ny < 0:
                        locs_by_garden[gx, gy - 1].add((nx, ny + garden.height))
                    elif ny >= garden.height:
                        locs_by_garden[gx, gy + 1].add((nx, ny - garden.height))
                    else:
                        locs_by_garden[gx, gy].add((nx, ny))
        for g in tracking_garden_traces:
            idx = tracking_garden_traces[g]
            if flip_flops[idx]:
                continue
            trace = traces[idx]
            trace.append(len(locs_by_garden[g]))
            if trace[-2:] == trace[-4:-2]:
                print(f"{step}: Cycle! {g} {trace[-2:]} at {len(trace)}")
                flip_flops[idx] = (len(trace), trace[-1], trace[-2])
                traces[idx] = None
            del trace
        # if flip_flops and all(flip_flops):
        #     del traces
        #     del start_traces
        #     break
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

    x1, y1 = 0, 0
    x2, y2 = 0, 0
    for x, y in state_by_garden:
        x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, x), max(y2, y)

    # noinspection PyUnboundLocalVariable
    sb = [f"after {step} steps across {len(locs_by_garden)} gardens"]
    for y in range(y1, y2 + 1):
        sb.append("\n")
        for x in range(x1, x2 + 1):
            g = x, y
            sb.append(f"{state_by_garden[g][1] if g in state_by_garden else '':3}")
        sb.append("    ")
        for x in range(x1, x2 + 1):
            g = x, y
            sb.append(f"{state_by_garden[g][0] if g in state_by_garden else '':4}")
    print("".join(sb))

    return sum(len(ls) for ls in locs_by_garden.values())


# after 393 steps across 37 gardens
#            3                         327
#         4  3  5                  262 196 262
#      4  4  3  5  5           262 131  65 131 262
#   1  1  1     0  0  0    327 196  65      65 196 327
#      6  6  2  7  7           262 131  65 131 262
#         6  2  7                  262 196 262
#            2                         327

if __name__ == "__main__":
    aoc.solve(
        __file__,
        Garden,
        part_one,
        part_two,
    )

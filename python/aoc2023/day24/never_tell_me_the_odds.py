from util import aoc


def parse(input):
    # 19, 13, 30 @ -2,  1, -2
    lines = input.replace(" ", "").splitlines()
    result = []
    for l in lines:
        p, v = (tuple(int(n) for n in c.split(",")) for c in l.split("@"))
        result.append((p, v))
    return result


def part_one(hailstorm, lo=200_000_000_000_000, hi=400_000_000_000_000):
    eqs = []
    for p, v in hailstorm:
        (x, y, _), (dx, dy, _) = p, v
        m = dy / dx
        tyi = -x / dx
        b = y + tyi * dy
        eqs.append((p, v, m, b))
    del p, v, x, y, dx, dy, m, tyi, b

    count = 0
    for i, (p1, v1, m1, b1) in enumerate(eqs):
        for p2, v2, m2, b2 in eqs[i + 1 :]:
            denom = m1 - m2
            if denom == 0:
                continue  # parallel
            x = (b2 - b1) / denom
            y = m2 * x + b2
            if lo <= x <= hi and lo <= y <= hi:
                t1 = (x - p1[0]) / v1[0]
                t2 = (x - p2[0]) / v2[0]
                if t1 >= 0 and t2 >= 0:
                    count += 1

    return count


# def part_two(model):
#     return None


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        # part_two,
    )

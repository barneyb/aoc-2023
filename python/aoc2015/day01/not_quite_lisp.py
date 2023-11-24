def both_parts(input):
    floor = 0
    pos = -1
    i = 0
    for c in input:
        i += 1
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            raise RuntimeError("Unknown '" + c + "'")
        if floor == -1 and pos == -1:
            pos = i
    return floor, pos


if __name__ == "__main__":
    from aocd import get_data

    print(both_parts(get_data(year=2015, day=1)))

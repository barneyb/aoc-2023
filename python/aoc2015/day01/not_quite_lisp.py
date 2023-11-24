from aocd import get_data


def get_input():
    return get_data(day=1, year=2015)


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


print(both_parts(get_input()))

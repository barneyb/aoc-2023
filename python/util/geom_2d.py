def move(pos, d, n=1):
    x, y = pos
    match d:
        case 0:
            return x, y - n
        case 1:
            return x + n, y
        case 2:
            return x, y + n
        case 3:
            return x - n, y

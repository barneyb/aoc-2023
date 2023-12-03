def parse_chars(string, convert=None):
    """Returns a (width,height,elements) tuple, built character by character
    from the string, passing each to the convert function (if not None).
    """
    w = None
    items = []
    if convert is None:
        convert = lambda it: it
    for line in string.splitlines():
        items.extend(convert(o) for o in line)
        if w is None:
            w = len(items)
    return w, len(items) // w, items


def unparse_chars(items, width, convert=str):
    """Returns a multiline string, built item by item, using the passed convert
    function to stringify each in turn.
    """
    sb = []
    end_of_line = width - 1
    for i, o in enumerate(items):
        sb.append(convert(o))
        if i % width == end_of_line:
            sb.append("\n")
    return "".join(sb)


class LinearGrid:
    def __init__(self, width, height):
        """Construct a new LinearGrid with the specified width and height. 'i'
        refers to an index in the element list. 'x' andn 'y' refer to planar
        coordinates, and 'p' refers to an (x,y) tuple (a point).
        """
        super().__init__()
        self.w = width
        self.h = height

    def to_i(self, p):
        """Convert the point to an index."""
        x, y = p
        return y * self.w + x

    def to_point(self, i):
        """Convert the index to a point."""
        return i % self.w, i // self.w

    def neighbors(self, p):
        """Return an iterable of the eight points around the given point. Some
        may be outside the grid's bounds.
        """
        x, y = p
        # note: start top-left and read around p clockwise.
        return [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x - 1, y),
        ]

    def neighbors_rect(self, p):
        """Return an iterable of the four points rectilinear-adjacent to the
        given point. Some may be outside the grid's bounds.
        """
        return [p for i, p in enumerate(self.neighbors(p)) if i % 2 == 1]

    def neighbors_diag(self, p):
        """Return an iterable of the four points diagonally-adjacent to the
        given point. Some may be outside the grid's bounds.
        """
        return [p for i, p in enumerate(self.neighbors(p)) if i % 2 == 0]

    def in_bounds(self, p):
        """Return whether the passed point is within the grid"""
        x, y = p
        return 0 <= x < self.w and 0 <= y < self.h

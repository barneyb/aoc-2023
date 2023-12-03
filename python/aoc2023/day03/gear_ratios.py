from util import aoc


class Schematic:
    def __init__(self, input):
        super().__init__()
        self.schematic = input.splitlines()
        self.w = len(self.schematic[0])
        self.h = len(self.schematic)

    def __eq__(self, other):
        return self.schematic == other

    def __str__(self):
        return "\n".join(self.schematic)

    def __contains__(self, p):
        x, y = p
        return 0 <= x < self.w and 0 <= y < self.h

    def __getitem__(self, p):
        x, y = p
        return self.schematic[y][x]

    def neighbors(self, p):
        """Returns the neighbors of the given point. Corners have three, edges
        have five, and the rest have eight.
        """
        x, y = p
        return filter(
            lambda p: p in self,
            [
                (x - 1, y - 1),
                (x, y - 1),
                (x + 1, y - 1),
                (x + 1, y),
                (x + 1, y + 1),
                (x, y + 1),
                (x - 1, y + 1),
                (x - 1, y),
            ],
        )

    def get_number_and_pos(self, p):
        """Returns the number and the position it starts at, given the location
        of an arbitrary digit within the number.
        """
        x, y = p
        line = self.schematic[y]
        start = x
        while start >= 0 and line[start].isdigit():
            start -= 1
        end = x
        while end < len(line) and line[end].isdigit():
            end += 1
        x = start + 1
        return int(line[x:end]), (x, y)

    def find_symbols(self):
        symbols = {}
        for y, line in enumerate(self.schematic):
            for x, c in enumerate(line):
                if c == "." or c.isdigit():
                    continue
                if c not in symbols:
                    symbols[c] = []
                symbols[c].append((x, y))
        return symbols

    def adjacent_numbers(self, p):
        locations = set()
        for p in self.neighbors(p):
            if self[p].isdigit():
                n, p = self.get_number_and_pos(p)
                if p not in locations:
                    locations.add(p)
                    yield n


def parse(input):
    return Schematic(input)


def part_one(schematic):
    total = 0
    for ps in schematic.find_symbols().values():
        for p in ps:
            for n in schematic.adjacent_numbers(p):
                total += n
    return total


def part_two(schematic):
    total = 0
    for p in schematic.find_symbols()["*"]:
        nums = list(schematic.adjacent_numbers(p))
        if len(nums) == 2:
            total += nums[0] * nums[1]
    return total


if __name__ == "__main__":
    aoc.solve(
        __file__,
        parse,
        part_one,
        part_two,
    )

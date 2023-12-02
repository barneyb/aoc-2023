class Screen:
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.length = width * height
        self.pixels = [False] * self.length

    def _xy2i(self, x, y):
        while x < 0:
            x += self.width
        x %= self.width
        while y < 0:
            y += self.length
        i = y * self.width % self.length + x
        assert 0 <= i < self.length
        return i % self.length

    def _i2xy(self, i):
        return i % self.width, i // self.width

    def _munge_i(self, i, dx, dy):
        x, y = self._i2xy(i)
        return self._xy2i(x + dx, y + dy)

    def execute(self, instructions):
        """I execute the passed instructions to update the screen. Instructions
        are always three-tuples with an opcode (rect, row, or col) and two
        integers (a and b) whose meaning vary by opcode.
        """
        for ins, a, b in instructions:
            match ins:
                case "rect":
                    self.pixels = [
                        True if i % self.width < a and i // self.width < b else p
                        for i, p in enumerate(self.pixels)]
                case "row":
                    self.pixels = [
                        self.pixels[self._munge_i(i, -b, 0)] if i // self.width == a else p
                        for i, p in enumerate(self.pixels)]
                case "col":
                    self.pixels = [
                        self.pixels[self._munge_i(i, 0, -b)] if i % self.width == a else p
                        for i, p in enumerate(self.pixels)]
                    pass

    def lit_pixel_count(self):
        """I return number of pixels which are currently lit/on."""
        return sum(1 if p else 0 for p in self.pixels)

    def __str__(self, *, on="#", off="."):
        """I convert this Screen to a string with 'height' lines and 'width'
        characters per line, with no trailing newline. On pixels are shown as
        '#' and off pixels are shown as '.'. This can be overridden via params.
        """
        pixels = []
        for y in range(self.height):
            if y > 0:
                pixels.append("\n")
            row = y * self.width
            for x in range(self.width):
                pixels.append(on if self.pixels[row + x] else off)
        return "".join(pixels)

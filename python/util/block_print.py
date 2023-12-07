"""I attempt to take block printing (a la 2016/08 Two-Factor Authentication) and
turn it into an equivalent string of ASCII letters. All block printed strings
are six rows 'tall', and fixed-width at five columns.

I don't yet understand the full AoC font, but I understand enough to get
Barney's answers. No guessing is performed; exact match only.
"""
import re

from .aoc import BLOCK

SPACE = " "
COLS = 5
ROWS = 6
RE_PRINT = re.compile(r"[^ ]")


def read(string: str):
    """Given a block-printed string, read the letters out of it. Spaces and
    periods are considered "blank"; all other characters are considered
    "marked". Leading and trailing newlines will be stripped.
    """
    string = string.replace(".", SPACE)
    rows = [RE_PRINT.sub(BLOCK, r) for r in string.strip("\n\r").splitlines()]
    assert len(rows) == ROWS, "not six rows tall"
    assert len(set(len(r) for r in rows)) == 1, "rows vary in length"
    assert all(len(r) % COLS == 0 for r in rows), "not multiple-of-five wide"
    result = []
    for i in range(0, len(rows[0]), COLS):
        glyph = "\n".join([r[i : i + 5] for r in rows])
        if glyph in GLYPHS:
            result.append(GLYPHS[glyph])
        else:
            raise RuntimeError("Unknown block printing glyph: \n" + glyph)
    return "".join(result)


C = """\
 ██  
█  █ 
█    
█    
█  █ 
 ██  """
H = """\
█  █ 
█  █ 
████ 
█  █ 
█  █ 
█  █ """
J = """\
  ██ 
   █ 
   █ 
   █ 
█  █ 
 ██  """
K = """\
█  █ 
█ █  
██   
█ █  
█ █  
█  █ """
L = """\
█    
█    
█    
█    
█    
████ """
P = """\
███  
█  █ 
█  █ 
███  
█    
█    """
R = """\
███  
█  █ 
█  █ 
███  
█ █  
█  █ """
U = """\
█  █ 
█  █ 
█  █ 
█  █ 
█  █ 
 ██  """
Y = """\
█   █
█   █
 █ █ 
  █  
  █  
  █  """
Z = """\
████ 
   █ 
  █  
 █   
█    
████ """


GLYPHS = {
    C: "C",
    H: "H",
    J: "J",
    K: "K",
    L: "L",
    P: "P",
    R: "R",
    U: "U",
    Y: "Y",
    Z: "Z",
}

from balance_bots import *

EXAMPLE = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

MODEL = (
    [(5, 2),
     (3, 1),
     (2, 2)],
    {2: (1, 0),
     1: (OUTPUT + 1, 0),
     0: (OUTPUT + 2, OUTPUT + 0)}
)


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_simulate():
    assert simulate(MODEL, 2, 5) == (2, [5, 2, 3])


def test_both_parts():
    assert both_parts(MODEL, 2, 5) == (2, 30)

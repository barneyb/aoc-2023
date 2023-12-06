from if_you_give_a_seed_a_fertilizer import *

# fmt: off
EXAMPLE = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

MODEL = (
    (79, 14, 55, 13),
    {"seed": ("soil", [
         (52, 50, 48),
         (50, 98,  2),],),
     "soil": ("fertilizer", [
         (39,  0, 15),
         ( 0, 15, 37),
         (37, 52,  2),],),
     "fertilizer": ("water", [
         (42,  0,  7),
         (57,  7,  4),
         ( 0, 11, 42),
         (49, 53,  8),],),
     "water": ("light", [
         (88, 18,  7),
         (18, 25, 70),],),
     "light": ("temperature", [
         (81, 45, 19),
         (68, 64, 13),
         (45, 77, 23),],),
     "temperature": ("humidity", [
         ( 1,  0, 69),
         ( 0, 69, 1),],),
     "humidity": ("location", [
         (60, 56, 37),
         (56, 93,  4),],),},)
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_convert():
    seed2soil = MODEL[1]["seed"]
    assert convert([(79, 80)], seed2soil) == [(81, 82)]
    assert convert([(14, 15)], seed2soil) == [(14, 15)]
    assert convert([(55, 56)], seed2soil) == [(57, 58)]


def test_convert_to_light():
    assert convert([(81, 82)], MODEL[1]["water"]) == [(74, 75)]


def test_to_location():
    mappings = linearize(MODEL[1])
    assert to_locations([(79, 80)], mappings) == [(82, 83)]
    assert to_locations([(14, 15)], mappings) == [(43, 44)]
    assert to_locations([(55, 56)], mappings) == [(86, 87)]
    assert to_locations([(13, 14)], mappings) == [(35, 36)]


def test_example_one():
    assert part_one(MODEL) == 35


def test_example_two():
    assert part_two(MODEL) == 46

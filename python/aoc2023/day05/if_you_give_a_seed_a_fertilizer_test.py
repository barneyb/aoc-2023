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
    {"seed": ( "soil", [
         (50, 98, 2),
         (52, 50, 48),],),
     "soil": ( "fertilizer", [
         (0, 15, 37),
         (37, 52, 2),
         (39, 0, 15),],),
     "fertilizer": ( "water", [
         (49, 53, 8),
         (0, 11, 42),
         (42, 0, 7),
         (57, 7, 4),],),
     "water": ( "light", [
         (88, 18, 7),
         (18, 25, 70),],),
     "light": ( "temperature", [
         (45, 77, 23),
         (81, 45, 19),
         (68, 64, 13),],),
     "temperature": ( "humidity", [
         (0, 69, 1),
         (1, 0, 69),],),
     "humidity": ( "location", [
         (60, 56, 37),
         (56, 93, 4),],),},)
# fmt: on


def test_parse():
    assert parse(EXAMPLE) == MODEL


def test_convert():
    seed2soil = MODEL[1]["seed"]
    assert convert(79, seed2soil) == 81
    assert convert(14, seed2soil) == 14
    assert convert(55, seed2soil) == 57


def test_convert_to_light():
    assert convert(81, MODEL[1]["water"]) == 74


def test_to_location():
    mappings = linearize(MODEL[1])
    assert to_location(79, mappings) == 82
    assert to_location(14, mappings) == 43
    assert to_location(55, mappings) == 86
    assert to_location(13, mappings) == 35


def test_example_one():
    assert part_one(MODEL) == 35


# def test_example_two():
#    assert part_two(MODEL) == 3

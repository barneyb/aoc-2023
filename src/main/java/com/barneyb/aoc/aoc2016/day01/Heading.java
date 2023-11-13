package com.barneyb.aoc.aoc2016.day01;

public enum Heading {
    NORTH,
    EAST,
    SOUTH,
    WEST;

    public Heading turn(Turn t) {
        Heading[] values = Heading.values();
        return values[(ordinal() + values.length + switch (t) {
            case RIGHT -> 1;
            case LEFT -> -1;
        }) % values.length];
    }
}

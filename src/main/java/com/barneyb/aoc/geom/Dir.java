package com.barneyb.aoc.geom;

public enum Dir {
    NORTH,
    EAST,
    SOUTH,
    WEST;

    public static Dir parse(char c) {
        return switch (c) {
            case 'n', 'N', 'u', 'U' -> NORTH;
            case 'e', 'E', 'r', 'R' -> EAST;
            case 's', 'S', 'd', 'D' -> SOUTH;
            case 'w', 'W', 'l', 'L' -> WEST;
            default -> throw new IllegalArgumentException(String.format(
                    "Unknown '%s' dir",
                    c));
        };
    }

    public Dir turn(Turn t) {
        Dir[] values = Dir.values();
        return values[(ordinal() + values.length + switch (t) {
            case RIGHT -> 1;
            case LEFT -> -1;
        }) % values.length];
    }
}

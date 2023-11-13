package com.barneyb.aoc.geom;

public enum Turn {
    LEFT,
    RIGHT;

    public static Turn parse(char c) {
        return switch (c) {
            case 'l', 'L' -> LEFT;
            case 'r', 'R' -> RIGHT;
            default -> throw new IllegalArgumentException(String.format(
                    "Unknown '%s' turn",
                    c));
        };
    }
}

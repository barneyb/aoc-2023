package com.barneyb.aoc.aoc2016.day01;

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

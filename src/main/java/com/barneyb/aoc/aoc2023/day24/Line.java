package com.barneyb.aoc.aoc2023.day24;

public record Line(double m, double b) {

    public static Line of(long x, long y, long dx, long dy) {
        return new Line((double) dy / dx,
                        y + (double) -x / dx * dy);
    }

}

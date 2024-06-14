package com.barneyb.aoc.aoc2023.day24;

public record Line(double m, double b) {

    Line(long x, long y, long dx, long dy) {
        this((double) dy / dx,
             y + (double) -x / dx * dy);
    }

}

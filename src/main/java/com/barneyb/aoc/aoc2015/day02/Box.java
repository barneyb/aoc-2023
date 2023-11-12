package com.barneyb.aoc.aoc2015.day02;

public record Box(long l, long w, long h) {

    public long paperRequired() {
        long a = l * w;
        long b = w * h;
        long c = h * l;
        return 2 * a + 2 * b + 2 * c + Math.min(a, Math.min(b, c));
    }

    public long ribbonRequired() {
        long v = l * w * h;
        long a = l + w;
        long b = w + h;
        long c = h + l;
        return v + 2 * Math.min(a, Math.min(b, c));
    }

}

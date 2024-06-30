package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.geom.Point3;

public record Hailstone(Point3 pos, Point3 vel) {

    public Line xy() {
        return Line.of(pos().x(), pos().y(), vel().x(), vel().y());
    }

    public Line xz() {
        return Line.of(pos().x(), pos().z(), vel().x(), vel().z());
    }

    public Line yz() {
        return Line.of(pos().y(), pos().z(), vel().y(), vel().z());
    }

}


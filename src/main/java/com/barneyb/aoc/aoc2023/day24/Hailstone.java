package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.geom.Point3;

public record Hailstone(Point3 pos, Point3 vel) {

    public Line xy() {
        return new Line(pos().x(), pos().y(), vel().x(), vel().y());
    }

    public Line xz() {
        return new Line(pos().x(), pos().z(), vel().x(), vel().z());
    }

    public Line yz() {
        return new Line(pos().y(), pos().z(), vel().y(), vel().z());
    }

}


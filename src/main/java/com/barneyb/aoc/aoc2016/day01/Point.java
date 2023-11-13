package com.barneyb.aoc.aoc2016.day01;

public record Point(long x, long y) {

    public static final Point ORIGIN = new Point(0, 0);

    public long manhattanDistance() {
        return manhattanDistance(ORIGIN);
    }

    public long manhattanDistance(Point other) {
        return Math.abs(x - other.x)
                + Math.abs(y - other.y);
    }

    public Point move(Heading h, Long distance) {
        return sum(switch (h) {
            case NORTH -> new Point(0, -distance);
            case EAST -> new Point(distance, 0);
            case SOUTH -> new Point(0, distance);
            case WEST -> new Point(-distance, 0);
        });
    }

    public Point sum(Point p) {
        return new Point(x + p.x,
                         y + p.y);
    }

}

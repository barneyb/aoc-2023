package com.barneyb.aoc.geom;

/**
 * A point in the plane. Note that coordinates work like in computer graphics,
 * not like in math: origin is top-left and y increases as you move south.
 */
public record Point(long x, long y) {

    public static Point of(long x, long y) {
        return new Point(x, y);
    }

    public static final Point ORIGIN = new Point(0, 0);

    public static Point parse(String str) {
        var coords = str.split(",");
        return new Point(Long.parseLong(coords[0]),
                         Long.parseLong(coords[1]));
    }

    public long manhattanDistance() {
        return manhattanDistance(ORIGIN);
    }

    public long manhattanDistance(Point other) {
        return Math.abs(x - other.x)
               + Math.abs(y - other.y);
    }

    public Point move(Dir dir) {
        return move(dir, 1L);
    }

    public Point move(Dir dir, Long distance) {
        return sum(switch (dir) {
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

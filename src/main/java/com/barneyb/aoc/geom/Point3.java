package com.barneyb.aoc.geom;

public record Point3(long x, long y, long z) {

    public static final Point3 ORIGIN = of(0, 0, 0);

    public static Point3 of(long x, long y, long z) {
        return new Point3(x, y, z);
    }

    public static Point3 parse(String str) {
        var coords = str.split(",");
        return of(Long.parseLong(coords[0].trim()),
                  Long.parseLong(coords[1].trim()),
                  Long.parseLong(coords[2].trim()));
    }

    public Point xy() {
        return new Point(x, y);
    }

    public Point xz() {
        return new Point(x, z);
    }

    public Point yz() {
        return new Point(y, z);
    }

    public Point3 multiply(long l) {
        return Point3.of(x * l, y * l, z * l);
    }

    public Point3 add(Point3 p) {
        return Point3.of(x + p.x, y + p.y, z + p.z);
    }

}

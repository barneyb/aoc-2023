package com.barneyb.aoc.geom;

public record Point3(long x, long y, long z) {

    public static final Point3 ORIGIN = new Point3(0, 0, 0);

    public static Point3 parse(String str) {
        var coords = str.split(",");
        return new Point3(Long.parseLong(coords[0].trim()),
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

}

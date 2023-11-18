package com.barneyb.aoc.geom;

import com.barneyb.aoc.util.Range;

import java.util.Iterator;

public record Line(Point a, Point b) implements Iterable<Point> {

    public boolean isVertical() {
        return a.x() == b.x();
    }

    public boolean isHorizontal() {
        return a.y() == b.y();
    }

    public Range xRange() {
        return new Range(a.x(), b.x());
    }

    public Range yRange() {
        return new Range(a.y(), b.y());
    }

    public Iterator<Point> points() {
        Range xr = xRange();
        if (isHorizontal()) {
            return new Horiz(xr, a.y());
        } else if (isVertical()) {
            return new Vert(a.x(), yRange());
        }
        Range yr = yRange();
        if (xr.size() == yr.size()) {
            return new Diag(xr, yr);
        } else {
            throw new UnsupportedOperationException(
                    "Only vertical, horizontal, and 45-degree lines can iterate over their points");
        }
    }

    /**
     * Alias of {@link #points()} for for-each support.
     */
    @Override
    public Iterator<Point> iterator() {
        return points();
    }

    private static class Horiz implements Iterator<Point> {

        private final Iterator<Long> xs;
        private final long y;

        public Horiz(Range xr, long y) {
            this.xs = xr.iterator();
            this.y = y;
        }

        @Override
        public boolean hasNext() {
            return xs.hasNext();
        }

        @Override
        public Point next() {
            return new Point(xs.next(), y);
        }

    }

    private static class Vert implements Iterator<Point> {

        private final long x;
        private final Iterator<Long> ys;

        public Vert(long x, Range yr) {
            this.x = x;
            this.ys = yr.iterator();
        }

        @Override
        public boolean hasNext() {
            return ys.hasNext();
        }

        @Override
        public Point next() {
            return new Point(x, ys.next());
        }

    }

    private static class Diag implements Iterator<Point> {

        private final Iterator<Long> xs;
        private final Iterator<Long> ys;

        public Diag(Range xr, Range yr) {
            assert xr.size() == yr.size() : "Line isn't at 45 degrees";
            this.xs = xr.iterator();
            this.ys = yr.iterator();
        }

        @Override
        public boolean hasNext() {
            return xs.hasNext() && ys.hasNext();
        }

        @Override
        public Point next() {
            return new Point(xs.next(), ys.next());
        }

    }

}

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
        if (isHorizontal()) {
            return new Horiz();
        } else if (isVertical()) {
            return new Vert();
        } else {
            throw new UnsupportedOperationException("Only vertical and horizontal lines can iterate over their points");
        }
    }

    /**
     * Alias of {@link #points()} for for-each support.
     */
    @Override
    public Iterator<Point> iterator() {
        return points();
    }

    private class Horiz implements Iterator<Point> {

        private final Iterator<Long> xs = xRange().iterator();
        private final long y = a.y();

        @Override
        public boolean hasNext() {
            return xs.hasNext();
        }

        @Override
        public Point next() {
            return new Point(xs.next(), y);
        }

    }

    private class Vert implements Iterator<Point> {

        private final long x = a.x();
        private final Iterator<Long> ys = yRange().iterator();

        @Override
        public boolean hasNext() {
            return ys.hasNext();
        }

        @Override
        public Point next() {
            return new Point(x, ys.next());
        }

    }

}

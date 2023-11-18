package com.barneyb.aoc.util;

import java.util.Iterator;

/**
 * I represent a range where both endpoints are included.
 */
public record Range(Long a, Long b) implements Iterable<Long> {

    public Range(int a, int b) {
        this((long) a, (long) b);
    }

    public long size() {
        return Math.abs(b - a) + 1; // closed
    }

    @Override
    public Iterator<Long> iterator() {
        return a <= b
                ? new CountUp()
                : new CountDown();
    }

    private class CountUp implements Iterator<Long> {

        private Long curr = a;

        @Override
        public boolean hasNext() {
            return curr <= b;
        }

        @Override
        public Long next() {
            return curr++;
        }

    }

    private class CountDown implements Iterator<Long> {

        private Long curr = a;

        @Override
        public boolean hasNext() {
            return curr >= b;
        }

        @Override
        public Long next() {
            return curr--;
        }

    }

}

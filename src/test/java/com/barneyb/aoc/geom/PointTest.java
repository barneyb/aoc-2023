package com.barneyb.aoc.geom;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class PointTest {

    @Test
    void parse() {
        var p = Point.parse("1,-2");
        assertEquals(1, p.x());
        assertEquals(-2, p.y());
    }

    @Test
    void manhattan() {
        assertEquals(0L, Point.ORIGIN.manhattanDistance());
        assertEquals(2L, new Point(2, 0).manhattanDistance());
        assertEquals(2L, new Point(0, 2).manhattanDistance());
        assertEquals(5L, new Point(2, 3).manhattanDistance());
    }

}

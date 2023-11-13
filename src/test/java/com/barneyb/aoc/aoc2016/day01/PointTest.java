package com.barneyb.aoc.aoc2016.day01;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class PointTest {

    @Test
    void manhattan() {
        assertEquals(0L, Point.ORIGIN.manhattanDistance());
        assertEquals(2L, new Point(2, 0).manhattanDistance());
        assertEquals(2L, new Point(0, 2).manhattanDistance());
        assertEquals(5L, new Point(2, 3).manhattanDistance());
    }

}

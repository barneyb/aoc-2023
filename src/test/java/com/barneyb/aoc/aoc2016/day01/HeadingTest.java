package com.barneyb.aoc.aoc2016.day01;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class HeadingTest {

    @Test
    void turn() {
        assertEquals(Heading.WEST, Heading.NORTH.turn(Turn.LEFT));
        assertEquals(Heading.EAST, Heading.NORTH.turn(Turn.RIGHT));
    }

}

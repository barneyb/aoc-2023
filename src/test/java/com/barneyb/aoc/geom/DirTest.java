package com.barneyb.aoc.geom;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class DirTest {

    @Test
    void turn() {
        assertEquals(Dir.WEST, Dir.NORTH.turn(Turn.LEFT));
        assertEquals(Dir.EAST, Dir.NORTH.turn(Turn.RIGHT));
    }

}

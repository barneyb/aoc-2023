package com.barneyb.aoc.aoc2022.day05;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MoveTest {

    @Test
    void parse() {
        var m = Move.parse("move 3 from 2 to 1");
        assertEquals(3, m.count());
        assertEquals(2, m.from());
        assertEquals(1, m.to());
    }

}

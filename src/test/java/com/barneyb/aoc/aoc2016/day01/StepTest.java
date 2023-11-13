package com.barneyb.aoc.aoc2016.day01;

import com.barneyb.aoc.geom.Turn;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class StepTest {

    @Test
    void parse() {
        Step s = Step.parse("R123");
        assertEquals(Turn.RIGHT, s.turn());
        assertEquals(123, s.distance());
    }

}

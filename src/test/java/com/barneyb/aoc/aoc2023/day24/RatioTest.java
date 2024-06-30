package com.barneyb.aoc.aoc2023.day24;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class RatioTest {

    @Test
    void add() {
        assertEquals(Ratio.of(3, 2),
                     Ratio.of(1, 2)
                             .add(1));
        assertEquals(Ratio.of(3, 4),
                     Ratio.of(1, 2)
                             .add(Ratio.of(1, 4)));
        assertEquals(Ratio.of(1, 4),
                     Ratio.of(1, 2)
                             .add(Ratio.of(-1, 4)));
        assertEquals(Ratio.of(-1, 4),
                     Ratio.of(1, -2)
                             .add(Ratio.of(1, 4)));
    }

    @Test
    void multiply() {
        assertEquals(Ratio.of(1, 4),
                     new Ratio(1, 8)
                             .multiply(2));
        assertEquals(Ratio.of(-1, 6),
                     Ratio.of(1, 2)
                             .multiply(Ratio.of(1, -3)));
    }

    @Test
    void divide() {
        assertEquals(Ratio.of(1, 4),
                     new Ratio(1, 2)
                             .divide(2));
        assertEquals(Ratio.of(-1, 3),
                     Ratio.of(1, 6)
                             .divide(Ratio.of(1, -2)));
    }

}

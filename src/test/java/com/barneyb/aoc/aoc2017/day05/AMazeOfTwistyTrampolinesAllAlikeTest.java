package com.barneyb.aoc.aoc2017.day05;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AMazeOfTwistyTrampolinesAllAlikeTest {

    @Test
    void solvePartOne() {
        var solver = new AMazeOfTwistyTrampolinesAllAlike();
        assertEquals(5,
                     solver.solvePartOne(new int[]{ 0, 3, 0, 1, -3 }));
    }

}

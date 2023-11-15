package com.barneyb.aoc.aoc2017.day05;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AMazeOfTwistyTrampolinesAllAlikeTest {

    @Test
    void solvePartOne() {
        var solver = new AMazeOfTwistyTrampolinesAllAlike();
        assertEquals(5,
                     solver.solvePartOne(List.of(0, 3, 0, 1, -3)));
    }

    @Test
    void solvePartTwo() {
        var solver = new AMazeOfTwistyTrampolinesAllAlike();
        assertEquals(10,
                     solver.solvePartTwo(List.of(0, 3, 0, 1, -3)));
    }

}

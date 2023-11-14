package com.barneyb.aoc.aoc2016.day05;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class HowAboutANiceGameOfChessTest {

    @Test
    void exampleOne() {
        assertEquals("18f47a30",
                     new HowAboutANiceGameOfChess()
                             .solvePartOne("abc"));
    }

    @Test
    void exampleTwo() {
        assertEquals("05ace8e3",
                     new HowAboutANiceGameOfChess()
                             .solvePartTwo("abc"));
    }

}

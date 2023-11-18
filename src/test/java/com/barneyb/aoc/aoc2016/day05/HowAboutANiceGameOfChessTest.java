package com.barneyb.aoc.aoc2016.day05;

import com.barneyb.aoc.CIOnly;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class HowAboutANiceGameOfChessTest {

    @Test
    void sequentialCode() {
        assertEquals("18",
                     new HowAboutANiceGameOfChess()
                             .sequentialCode("abc", 2));
    }

    @Test
    @CIOnly
    void exampleOne() {
        assertEquals("18f47a30",
                     new HowAboutANiceGameOfChess()
                             .solvePartOne("abc"));
    }

    @Test
    @CIOnly
    void exampleTwo() {
        assertEquals("05ace8e3",
                     new HowAboutANiceGameOfChess()
                             .solvePartTwo("abc"));
    }

    @Test
    @CIOnly
    void realWorld() {
        new HowAboutANiceGameOfChess().test("f97c354d", "863dde27");
    }

}

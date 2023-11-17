package com.barneyb.aoc.aoc2016.day05;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.condition.EnabledIfEnvironmentVariable;

import static org.junit.jupiter.api.Assertions.assertEquals;

@EnabledIfEnvironmentVariable(
        named = "CI",
        matches = "true",
        disabledReason = "Only in CI - too slow")
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

    @Test
    void realWorld() {
        new HowAboutANiceGameOfChess().test("f97c354d", "863dde27");
    }

}

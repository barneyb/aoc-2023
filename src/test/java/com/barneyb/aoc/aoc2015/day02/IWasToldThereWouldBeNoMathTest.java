package com.barneyb.aoc.aoc2015.day02;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class IWasToldThereWouldBeNoMathTest {

    @Test
    void examplesPartOne() {
        Long a = new IWasToldThereWouldBeNoMath()
                .solvePartOne(List.of(
                        new Box(2, 3, 4),
                        new Box(1, 1, 10)
                ));
        assertEquals(58L + 43, a);
    }

    @Test
    void examplesPartTwo() {
        Long a = new IWasToldThereWouldBeNoMath()
                .solvePartTwo(List.of(
                        new Box(2, 3, 4),
                        new Box(1, 1, 10)
                ));
        assertEquals(34L + 14, a);
    }

    @Test
    void realWorld() {
        new IWasToldThereWouldBeNoMath().test(1598415, 3812909);
    }

}

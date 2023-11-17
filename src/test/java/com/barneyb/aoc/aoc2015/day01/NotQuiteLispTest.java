package com.barneyb.aoc.aoc2015.day01;

import com.barneyb.aoc.util.Answers;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class NotQuiteLispTest {

    @Test
    void exampleFive() {
        Answers<Integer, Integer> as = new NotQuiteLisp().solveTogether(")))".toCharArray());
        assertEquals(-3, as.partOne());
        assertEquals(1, as.partTwo());
    }

    @Test
    void exampleSeven() {
        Answers<Integer, Integer> as = new NotQuiteLisp().solveTogether("()())".toCharArray());
        assertEquals(-1, as.partOne());
        assertEquals(5, as.partTwo());
    }

    @Test
    void realWorld() {
        new NotQuiteLisp().test(280, 1797);
    }

}

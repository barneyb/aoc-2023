package com.barneyb.aoc.aoc2022.day05;

import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SupplyStacksTest {

    private static final String EXAMPLE_ONE = """
                [D]   \s
            [N] [C]   \s
            [Z] [M] [P]
             1   2   3\s
                        
            move 1 from 2 to 1
            move 3 from 1 to 3
            move 2 from 2 to 1
            move 1 from 1 to 2""";

    private static final StacksAndMoves MODEL_ONE = new StacksAndMoves(
            Arrays.asList("ZN",
                          "MCD",
                          "P"),
            Arrays.asList(new Move(1, 2, 1),
                          new Move(3, 1, 3),
                          new Move(2, 2, 1),
                          new Move(1, 1, 2)));

    @Test
    void parsing() {
        assertEquals(MODEL_ONE,
                     new SupplyStacks().buildModel(
                             Input.of(EXAMPLE_ONE)));
    }

    @Test
    void exampleOne() {
        assertEquals("CMZ",
                     new SupplyStacks().solvePartOne(MODEL_ONE));
    }

    @Test
    void realWorld() {
        new SupplyStacks().test("PTWLTDSJV");
    }

}

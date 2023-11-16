package com.barneyb.aoc.aoc2018.day05;

import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AlchemicalReductionTest {

    @Test
    void exampleOne() {
        var solver = new AlchemicalReduction();
        var polymer = solver.buildModel(Input.of("dabAcCaCBAcCcaDA"));
        assertEquals(10, solver
                .solvePartOne(polymer));
    }

    @Test
    void exampleTwo() {
        var solver = new AlchemicalReduction();
        var polymer = solver.buildModel(Input.of("dabAcCaCBAcCcaDA"));
        assertEquals(4, solver
                .solvePartTwo(polymer));
    }

}

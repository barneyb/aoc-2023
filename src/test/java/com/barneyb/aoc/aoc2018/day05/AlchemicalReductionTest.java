package com.barneyb.aoc.aoc2018.day05;

import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AlchemicalReductionTest {

    @Test
    void exampleOne() {
        var solver = new AlchemicalReduction();
        var model = solver.buildModel(Input.of("dabAcCaCBAcCcaDA"));
        assertEquals(10, solver
                .solvePartOne(model));
    }

}

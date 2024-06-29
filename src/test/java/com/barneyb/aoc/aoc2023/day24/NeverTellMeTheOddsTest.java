package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class NeverTellMeTheOddsTest {

    private static final String EXAMPLE =
            """
            19, 13, 30 @ -2,  1, -2
            18, 19, 22 @ -1, -1, -2
            20, 25, 34 @ -2, -2, -4
            12, 31, 28 @ -1, -2, -1
            20, 19, 15 @  1, -5, -3
            """;

    @Test
    void exampleOne() {
        var solver = new NeverTellMeTheOdds();
        var model = solver.buildModel(Input.of(EXAMPLE));
        assertEquals(2, solver.solvePartOne(model, 7, 27));
    }

    @Test
    void exampleTwo() {
        var solver = new NeverTellMeTheOdds();
        var model = solver.buildModel(Input.of(EXAMPLE));
        assertEquals(47, solver.solvePartTwo(model));
    }

    @Test
    void realInput() {
        var solver = new NeverTellMeTheOdds();
        var model = solver.buildModel(Input.of(NeverTellMeTheOddsTest.class));
        assertEquals(18_651, solver.solvePartOne(model));
        //  x  = 200_027_938_836_082
        //  y  = 127_127_087_242_193
        //  z  = 219_339_468_239_370
        // dx =                  133
        // dy =                  278
        // dz =                   85
        //  t =       57_633_470_621 (first)
        //  t =    1_029_733_593_764 (last)
        assertEquals(546_494_494_317_645L, solver.solvePartTwo(model));
    }

}

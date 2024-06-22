package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.stream.Collectors;

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
    void realInput() {
        var solver = new NeverTellMeTheOdds();
        var model = solver.buildModel(Input.of(NeverTellMeTheOddsTest.class));
        assertEquals(18651, solver.solvePartOne(model));
        //todo assertEquals(-1, solver.solvePartTwo(model));
    }

    @Test
    void playing() {
        var solver = new NeverTellMeTheOdds();
//        var model = solver.buildModel(Input.of(EXAMPLE));
        var model = solver.buildModel(Input.of(NeverTellMeTheOdds.class));
        var vels = model.stream()
                .map(Hailstone::vel)
                .map(v -> {
                    var f = Factors.gcd(Factors.gcd(Math.abs(v.x()), Math.abs(v.y())), Math.abs(v.z()));
                    if (f > 1) {
                        v = v.divide(f);
                    }
                    return v;
                })
                .collect(Collectors.toSet());
        assertEquals(model.size(), vels.size());
        solver.solvePartTwo(model);
    }

}

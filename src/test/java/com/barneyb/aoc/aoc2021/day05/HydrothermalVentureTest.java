package com.barneyb.aoc.aoc2021.day05;

import com.barneyb.aoc.geom.Line;
import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Answers;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class HydrothermalVentureTest {

    private static final String EXAMPLE_ONE = """
            0,9 -> 5,9
            8,0 -> 0,8
            9,4 -> 3,4
            2,2 -> 2,1
            7,0 -> 7,4
            6,4 -> 2,0
            0,9 -> 2,9
            3,4 -> 1,4
            0,0 -> 8,8
            5,5 -> 8,2""";

    @Test
    void parse() {
        var lines = new HydrothermalVenture()
                .buildModel(Input.of("7,0 -> 3,4"));
        assertEquals(1, lines.size());
        var l = lines.get(0);
        assertEquals(new Point(7, 0), l.a());
        assertEquals(new Point(3, 4), l.b());
    }

    @Test
    void exampleOne() {
        var solver = new HydrothermalVenture();
        List<Line> lines = solver.buildModel(Input.of(EXAMPLE_ONE));
        assertEquals(new Answers<>(5, 12),
                     solver.solveTogether(lines));
    }

    @Test
    void realWorld() {
        new HydrothermalVenture().test(7644, 18627);
    }

}

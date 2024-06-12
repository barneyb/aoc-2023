package com.barneyb.aoc.aoc2023.day21;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class StepCounterTest {

    private static final String EXAMPLE_ONE =
            """
            ...........
            .....###.#.
            .###.##..#.
            ..#.#...#..
            ....#.#....
            .##..S####.
            .##..#...#.
            .......##..
            .##.#.####.
            .##..##.##.
            ...........
            """;

    @Test
    void parsing() {
        StepCounter solver = new StepCounter();
        StepCounter.Model model = solver.buildModel(Input.of(EXAMPLE_ONE));
        assertEquals(List.of(Point.of(5, 4),
                             Point.of(4, 5)),
                     model.graph().adjacent(model.start()));
        assertEquals(List.of(Point.of(3, 6),
                             Point.of(2, 7),
                             Point.of(4, 7),
                             Point.of(3, 8)),
                     model.graph().adjacent(Point.of(3, 7)));
        assertEquals(List.of(),
                     model.graph().adjacent(Point.of(7, 5)));
        assertEquals(List.of(),
                     model.graph().adjacent(Point.of(8, 8)));
    }

    @Test
    void examplesOne() {
        StepCounter solver = new StepCounter();
        StepCounter.Model model = solver.buildModel(Input.of(EXAMPLE_ONE));
        assertEquals(2, solver.solvePartOne(model, 1));
        assertEquals(4, solver.solvePartOne(model, 2));
        assertEquals(6, solver.solvePartOne(model, 3));
        assertEquals(16, solver.solvePartOne(model, 6));
    }

}

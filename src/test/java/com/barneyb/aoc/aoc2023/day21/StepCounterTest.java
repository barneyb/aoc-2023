package com.barneyb.aoc.aoc2023.day21;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class StepCounterTest {

    private static final String EXAMPLE =
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
        Model model = solver.buildModel(Input.of(EXAMPLE));
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
        Model model = solver.buildModel(Input.of(EXAMPLE));
        assertEquals(2, solver.solvePartOne(model, 1));
        assertEquals(4, solver.solvePartOne(model, 2));
        assertEquals(6, solver.solvePartOne(model, 3));
        assertEquals(16, solver.solvePartOne(model, 6));
    }

    @Test
    void examplesTwo() {
        StepCounter solver = new StepCounter();
        Model model = solver.buildModel(Input.of(EXAMPLE));
        assertEquals(16, solver.solvePartTwo(model, 6));
        assertEquals(50, solver.solvePartTwo(model, 10));
        assertEquals(1594, solver.solvePartTwo(model, 50));
        assertEquals(6536, solver.solvePartTwo(model, 100));
        assertEquals(167004, solver.solvePartTwo(model, 500));
        assertEquals(668697, solver.solvePartTwo(model, 1000));
        assertEquals(16733044, solver.solvePartTwo(model, 5000));
    }

}

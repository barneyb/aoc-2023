package com.barneyb.aoc.aoc2016.day01;

import com.barneyb.aoc.geom.Turn;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.Iterator;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

class NoTimeForATaxicabTest {

    @Test
    void parse() {
        Input in = Input.of("R5, L5, R5, R3");

        List<Step> steps = new NoTimeForATaxicab()
                .buildModel(in);

        Iterator<Step> itr = steps.iterator();
        assertEquals(Turn.RIGHT, itr.next().turn());
        assertEquals(Turn.LEFT, itr.next().turn());
        assertEquals(5L, itr.next().distance());
        assertEquals(3L, itr.next().distance());
        assertFalse(itr.hasNext());
    }

    @Test
    void partOne() {
        List<Step> steps = List.of(
                new Step(Turn.RIGHT, 2L),
                new Step(Turn.LEFT, 3L));

        Long distance = new NoTimeForATaxicab().solvePartOne(steps);

        assertEquals(5L, distance);
    }

    @Test
    void partTwo() {
        Input in = Input.of("R8, R4, R4, R8");
        NoTimeForATaxicab solver = new NoTimeForATaxicab();
        List<Step> steps = solver.buildModel(in);

        Long distance = solver.solvePartTwo(steps);

        assertEquals(4L, distance);
    }

}

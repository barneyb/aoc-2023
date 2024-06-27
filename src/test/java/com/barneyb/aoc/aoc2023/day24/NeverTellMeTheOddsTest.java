package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.CIOnly;
import com.barneyb.aoc.util.Input;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverSolutionCallback;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;
import com.google.ortools.sat.LinearArgument;
import com.google.ortools.sat.LinearExpr;
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
    @CIOnly
    void realInput() {
        var solver = new NeverTellMeTheOdds();
        var model = solver.buildModel(Input.of(NeverTellMeTheOddsTest.class));
        assertEquals(18_651, solver.solvePartOne(model));
        assertEquals(546_494_494_317_645L, solver.solvePartTwo(model));
    }

    private int count = 0;

    private String name(String prefix) {
        return prefix + count++;
    }

    private final long lo = Long.MIN_VALUE >> 14;
    private final long hi = Long.MAX_VALUE >> 14;

    private void doit(CpModel model, IntVar p, IntVar v, IntVar t, long pos, long vel) {
        // i = -v
        var i = model.newIntVar(lo, hi, name("i"));
        model.addMultiplicationEquality(i, v, LinearExpr.constant(-1));
        // j = -2 + i
        var j = model.newIntVar(lo, hi, name("j"));
        model.addEquality(j, LinearExpr.sum(new LinearArgument[]{ LinearExpr.constant(vel), i }));
        // k = j * t
        var k = model.newIntVar(lo, hi, name("k"));
        model.addMultiplicationEquality(k, j, t);
        // p = k + 19
        model.addEquality(p, LinearExpr.sum(new LinearArgument[]{ k, LinearExpr.constant(pos) }));
    }

    @Test
    void lakjdsf() {
        var start = System.currentTimeMillis();
        var ntmto = new NeverTellMeTheOdds();
        System.out.printf("Loaded libs/input %d ms%n", System.currentTimeMillis() - start);
        start = System.currentTimeMillis();
        var model = new CpModel();
        var x = model.newIntVar(lo, hi, "x");
        var y = model.newIntVar(lo, hi, "y");
        var z = model.newIntVar(lo, hi, "z");
        var a = model.newIntVar(lo, hi, "a");
        var b = model.newIntVar(lo, hi, "b");
        var c = model.newIntVar(lo, hi, "c");
        for (var h : ntmto.buildModel(Input.of(EXAMPLE))) {
            var t = model.newIntVar(0, hi, name("t"));
            doit(model, x, a, t, h.pos().x(), h.vel().x());
            doit(model, y, b, t, h.pos().y(), h.vel().y());
            doit(model, z, c, t, h.pos().z(), h.vel().z());
        }
        System.out.printf("built model in %d ms%n", System.currentTimeMillis() - start);
        start = System.currentTimeMillis();
        CpSolver solver = new CpSolver();
        CpSolverStatus status = solver.solve(model, new CpSolverSolutionCallback() {
            @Override
            public void onSolutionCallback() {
                System.out.printf("[%3.0f ms]", wallTime() * 1000);
                System.out.print(" x = " + value(x));
                System.out.print(", y = " + value(y));
                System.out.print(", z = " + value(z));
                System.out.print(", a = " + value(a));
                System.out.print(", b = " + value(b));
                System.out.print(", c = " + value(c));
                System.out.println();
            }
        });
        // 546494494317645
        if (status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE) {
            System.out.printf("[%3.0f ms]", solver.wallTime() * 1000);
            System.out.print(" x = " + solver.value(x));
            System.out.print(", y = " + solver.value(y));
            System.out.print(", z = " + solver.value(z));
            System.out.print(", a = " + solver.value(a));
            System.out.print(", b = " + solver.value(b));
            System.out.print(", c = " + solver.value(c));
            System.out.println();
            assertEquals(24, solver.value(x));
            assertEquals(13, solver.value(y));
            assertEquals(10, solver.value(z));
            assertEquals(-3, solver.value(a));
            assertEquals(1, solver.value(b));
            assertEquals(2, solver.value(c));
        } else {
            System.out.println("No solution found: " + status);
        }
        System.out.printf("solved in %d ms%n", System.currentTimeMillis() - start);
        System.out.println(model.modelStats());
        assert status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE;
        System.out.println(solver.responseStats());
    }

}

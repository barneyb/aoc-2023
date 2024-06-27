package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.geom.Point3;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;
import com.google.ortools.sat.LinearArgument;
import com.google.ortools.sat.LinearExpr;

import java.util.List;

public class NeverTellMeTheOdds extends SolveEachPart<List<Hailstone>, Long, Long> {

    static {
        Loader.loadNativeLibraries();
    }

    public static void main(String[] args) {
        new NeverTellMeTheOdds().solveAndPrint();
    }

    @Override
    protected Long solvePartOne(List<Hailstone> hailstones) {
        return solvePartOne(hailstones, 200_000_000_000_000L, 400_000_000_000_000L);
    }

    private int count = 0;
    private final long lo = Long.MIN_VALUE >> 14;
    private final long hi = Long.MAX_VALUE >> 14;

    private String name(String prefix) {
        return prefix + count++;
    }

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

    @Override
    protected Long solvePartTwo(List<Hailstone> hailstones) {
        var model = new CpModel();
        var x = model.newIntVar(lo, hi, "x");
        var y = model.newIntVar(lo, hi, "y");
        var z = model.newIntVar(lo, hi, "z");
        var a = model.newIntVar(lo, hi, "a");
        var b = model.newIntVar(lo, hi, "b");
        var c = model.newIntVar(lo, hi, "c");
        for (var h : hailstones) {
            var t = model.newIntVar(0, hi, name("t"));
            doit(model, x, a, t, h.pos().x(), h.vel().x());
            doit(model, y, b, t, h.pos().y(), h.vel().y());
            doit(model, z, c, t, h.pos().z(), h.vel().z());
        }
        CpSolver solver = new CpSolver();
        CpSolverStatus status = solver.solve(model);
        if (status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE) {
            System.out.printf("[%3.0f ms]", solver.wallTime() * 1000);
            System.out.print(" x = " + solver.value(x));
            System.out.print(", y = " + solver.value(y));
            System.out.print(", z = " + solver.value(z));
            System.out.print(", a = " + solver.value(a));
            System.out.print(", b = " + solver.value(b));
            System.out.print(", c = " + solver.value(c));
            System.out.println();
            return solver.value(x)
                   + solver.value(y)
                   + solver.value(z);
        } else {
            throw new RuntimeException("No solution found: " + status);
        }
    }

    @Override
    protected List<Hailstone> buildModel(Input input) {
        return input.streamLines()
                .map(l -> l.split("@"))
                .map(ps -> new Hailstone(Point3.parse(ps[0]),
                                         Point3.parse(ps[1])))
                .toList();
    }

    private record Eq(int i, Point pos, Point vel, Line l) {}

    public Long solvePartOne(List<Hailstone> hailstones, long min, long max) {
        var equations = new Eq[hailstones.size()];
        for (int i = 0; i < hailstones.size(); i++) {
            var s = hailstones.get(i);
            equations[i] = new Eq(i, s.pos().xy(), s.vel().xy(), s.xy());
        }

        long count = 0;
        for (int i = 0; i < equations.length; i++) {
            var a = equations[i];
            for (int j = i + 1; j < equations.length; j++) {
                var b = equations[j];
                var denom = a.l().m() - b.l().m();
                if (denom == 0) continue; // parallel
                var x = (b.l().b() - a.l().b()) / denom;
                if (x < min || x > max) continue;
                var y = b.l().m() * x + b.l().b();
                if (y < min || y > max) continue;
                var t1 = (x - a.pos().x()) / a.vel().x();
                if (t1 < 0) continue;
                var t2 = (x - b.pos().x()) / b.vel().x();
                if (t2 < 0) continue;
                count += 1;
            }
        }
        return count;
    }

}

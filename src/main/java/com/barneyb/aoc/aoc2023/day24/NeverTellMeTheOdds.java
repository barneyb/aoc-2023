package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.geom.Point3;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverSolutionCallback;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;
import com.google.ortools.sat.LinearExpr;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

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

    private static class Storm {

        private final long lo, hi;
        private final Map<String, Integer> counts = new HashMap<>();
        final List<IntVar> ofNote;
        final IntVar x, y, z, a, b, c;

        Storm(List<Hailstone> hailstones, CpModel model) {
            long lo = Long.MAX_VALUE;
            long hi = Long.MIN_VALUE;
            for (var h : hailstones) {
                var x = h.pos().x();
                var y = h.pos().y();
                var z = h.pos().z();
                lo = Math.min(lo, Math.min(x, Math.min(y, z)));
                hi = Math.max(hi, Math.max(x, Math.max(y, z)));
            }
            this.lo = lo = Math.min(Long.MIN_VALUE >> 13, lo);
            this.hi = hi = Math.min(Long.MAX_VALUE >> 13, hi);

            ofNote = new ArrayList<>(hailstones.size() + 6);
            ofNote.add(x = model.newIntVar(lo, hi, "x"));
            ofNote.add(y = model.newIntVar(lo, hi, "y"));
            ofNote.add(z = model.newIntVar(lo, hi, "z"));
            ofNote.add(a = model.newIntVar(lo, hi, "a"));
            ofNote.add(b = model.newIntVar(lo, hi, "b"));
            ofNote.add(c = model.newIntVar(lo, hi, "c"));
            for (Hailstone h : hailstones) {
                var t = model.newIntVar(0, hi - lo, name("t"));
                ofNote.add(t);
                addStoneDimension(model, x, a, t, h.pos().x(), h.vel().x());
                addStoneDimension(model, y, b, t, h.pos().y(), h.vel().y());
                addStoneDimension(model, z, c, t, h.pos().z(), h.vel().z());
            }
            ofNote.forEach(v -> model.addHint(v, 0));
        }

        private String name(String prefix) {
            return prefix + counts.compute(prefix,
                                           (p, i) -> i == null
                                                   ? 0
                                                   : (i + 1));
        }

        private void addStoneDimension(CpModel model, IntVar p, IntVar v, IntVar t, long pos, long vel) {
            // p = (vel + -v) * t + pos
            // i = -v
            var i = model.newIntVar(lo, hi, name("i"));
            model.addEquality(i, LinearExpr.term(v, -1));
            // j = vel + i
            var j = model.newIntVar(lo, hi, name("j"));
            model.addEquality(j, LinearExpr.affine(i, 1, vel));
            // k = j * t
            var k = model.newIntVar(lo, hi, name("k"));
            model.addMultiplicationEquality(k, j, t);
            // p = k + pos
            model.addEquality(p, LinearExpr.affine(k, 1, pos));
        }

    }

    private static class SolutionCallback extends CpSolverSolutionCallback {

        private final Storm storm;
        private final Set<Long> solutions = new HashSet<>();

        public Set<Long> getSolutions() {
            return solutions;
        }

        SolutionCallback(Storm storm) {
            this.storm = storm;
        }

        @Override
        public synchronized void onSolutionCallback() {
            long s = value(storm.x)
                     + value(storm.y)
                     + value(storm.z);
            if (!solutions.add(s)) {
                return;
            }
            System.out.println(solutions.size() == 1
                                       ? "Found solution!"
                                       : "Found another solution!");
            System.out.printf("[%3.0f ms]", wallTime() * 1000);
            System.out.print(" x = " + value(storm.x));
            System.out.print(", y = " + value(storm.y));
            System.out.print(", z = " + value(storm.z));
            System.out.print(", a = " + value(storm.a));
            System.out.print(", b = " + value(storm.b));
            System.out.print(", c = " + value(storm.c));
            for (var t : storm.ofNote) {
                System.out.printf(", %s = %d", t.getName(), value(t));
            }
            System.out.println();
        }

    }

    protected Long solvePartTwo(List<Hailstone> hailstones) {
        var model = new CpModel();
        var storm = new Storm(hailstones, model);
        CpSolver solver = new CpSolver();
//        solver.getParameters().setEnumerateAllSolutions(true);
        SolutionCallback cb = new SolutionCallback(storm);
        CpSolverStatus status = solver.solve(model, cb);
        if (cb.getSolutions().isEmpty()) {
            throw new RuntimeException("No solution found: " + status);
        }
        return cb.getSolutions().iterator().next();
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

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
import lombok.Getter;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class NeverTellMeTheOdds extends SolveEachPart<List<Hailstone>, Long, Long> {

    public static void main(String[] args) {
        new NeverTellMeTheOdds().solveAndPrint();
    }

    @Override
    protected Long solvePartOne(List<Hailstone> hailstones) {
        return solvePartOne(hailstones, 200_000_000_000_000L, 400_000_000_000_000L);
    }

    @Override
    protected Long solvePartTwo(List<Hailstone> hailstones) {
        return computePartTwo(hailstones);
    }

    private record Vec(BigInteger x, BigInteger y, BigInteger z) {

        public static Vec of(BigInteger x, BigInteger y, BigInteger z) {
            return new Vec(x, y, z);
        }

        public static Vec of(Point3 p) {
            return Vec.of(new BigInteger("" + p.x(), 10),
                          new BigInteger("" + p.y(), 10),
                          new BigInteger("" + p.z(), 10));
        }

        public Vec multiply(BigInteger l) {
            return Vec.of(x.multiply(l),
                          y.multiply(l),
                          z.multiply(l));
        }

        public Vec divide(BigInteger l) {
            return Vec.of(x.divide(l),
                          y.divide(l),
                          z.divide(l));
        }

        public Vec add(Vec p) {
            return Vec.of(x.add(p.x),
                          y.add(p.y),
                          z.add(p.z));
        }

        public Vec subtract(Vec p) {
            return Vec.of(x.subtract(p.x),
                          y.subtract(p.y),
                          z.subtract(p.z));
        }

        public BigInteger dot(Vec p) {
            return x.multiply(p.x)
                    .add(y.multiply(p.y))
                    .add(z.multiply(p.z));
        }

        public Vec cross(Vec p) {
            return Vec.of(y.multiply(p.z).subtract(z.multiply(p.y)),
                          z.multiply(p.x).subtract(x.multiply(p.z)),
                          x.multiply(p.y).subtract(y.multiply(p.x)));
        }

        public BigInteger manhattan() {
            return x.add(y).add(z);
        }

    }

    public long computePartTwo(List<Hailstone> model) {
        /*
         https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kxqjg33/

         A little linear algebra makes part 2 very straightforward. You don't even
         need to solve a system of equations. It helps to view everything relative
         to hailstone 0. Let position_x and velocity_x be the position and velocity
         of hailstone x.
        */
        Hailstone a = model.get(0),
                b = model.get(1),
                c = model.get(4);

        //Stones 1 and 2, relative to stone 0:
        var position_0 = Vec.of(a.pos());
        var velocity_0 = Vec.of(a.vel());
        var position_1 = Vec.of(b.pos());
        var velocity_1 = Vec.of(b.vel());
        var position_2 = Vec.of(c.pos());
        var velocity_2 = Vec.of(c.vel());
        var p1 = position_1.subtract(position_0);
        var v1 = velocity_1.subtract(velocity_0);
        var p2 = position_2.subtract(position_0);
        var v2 = velocity_2.subtract(velocity_0);
        /*
         NB: 'x' means "cross product" and '*' means "dot product". There is no
         variable named 'x' anywhere (the first field of the various vectors is
         never referenced directly).

         Hailstone 0 is always at the origin, thus its collision is at 0. Since
         all three collisions must form a straight line, the above two collision
         vectors must be collinear, and their cross product will be 0:

           (p1 + t1 * v1) x (p2 + t2 * v2) = 0

         Cross product is distributive with vector addition and compatible with
         scalar multiplication, so the above can be expanded:

           (p1 x p2) + t1 * (v1 x p2) + t2 * (p1 x v2) + t1 * t2 * (v1 x v2) = 0

         This is starting to look like a useful linear equation, except for that
         t1 * t2 term. Let's try to get rid of it. Dot product and cross product
         interact in a useful way. For arbitrary vectors a and b:

           (a x b) * a = (a x b) * b = 0.

         We can use this property to get rid of the t1 * t2 term. Let's take the
         dot product with v2. Note that dot product is also distributive with
         vector addition and compatible with scalar multiplication. The dot
         product zeros out both the t2 and t1*t2 terms, leaving a simple linear
         equation for t1:

           (p1 x p2) * v2 + t1 * (v1 x p2) * v2 = 0
           t1 = -((p1 x p2) * v2) / ((v1 x p2) * v2)

         If we use v1 instead of v2 for the dot product, we get this instead:

           (p1 x p2) * v1 + t2 * (p1 x v2) * v1 = 0
           t2 = -((p1 x p2) * v1) / ((p1 x v2) * v1)
         */
        var t1 = p1.cross(p2).dot(v2).negate().divide(v1.cross(p2).dot(v2));
        var t2 = p1.cross(p2).dot(v1).negate().divide(p1.cross(v2).dot(v1));
        /*
         Once we have t1 and t2 we can compute the locations (in absolute
         coordinates) of the two collisions...
         */
        var c1 = position_1.add(velocity_1.multiply(t1));
        var c2 = position_2.add(velocity_2.multiply(t2));
        /*
         ...and work backwards to find the velocity and then initial position of
         the rock.
         */
        var v = c2.subtract(c1).divide(t2.subtract(t1));
        var p = c1.subtract(v.multiply(t1));
        /*
         Add up the individual coordinates of the position for the answer:
         */
        return p.manhattan().longValue();
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
        @Getter
        private final Set<Long> solutions = new HashSet<>();

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

    protected Long constraintPartTwo(List<Hailstone> hailstones) {
        Loader.loadNativeLibraries();
        var model = new CpModel();
        var storm = new Storm(hailstones, model);
        CpSolver solver = new CpSolver();
        solver.getParameters().setEnumerateAllSolutions(false);
        solver.getParameters().setMaxMemoryInMb(32);
        solver.getParameters().setMaxTimeInSeconds(15.0);
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

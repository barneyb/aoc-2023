package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.geom.Point3;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.List;

public class NeverTellMeTheOdds extends SolveEachPart<List<Hailstone>, Long, Long> {

    public static void main(String[] args) {
//        new NeverTellMeTheOdds().solveAndPrint();

        var a = new Hailstone(Point3.of(19, 13, 30),
                              Point3.of(-2, 1, -2));
        var b = new Hailstone(Point3.of(18, 19, 22),
                              Point3.of(-1, -1, -2));
        var c = new Hailstone(Point3.of(20, 25, 34),
                              Point3.of(-2, -2, -4));
        var d = new Hailstone(Point3.of(12, 31, 28),
                              Point3.of(-1, -2, -1));
        var e = new Hailstone(Point3.of(20, 19, 15),
                              Point3.of(1, -5, -3));
        var rock = new Hailstone(Point3.of(24, 13, 10),
                                 Point3.of(-3, 1, 2));
//        System.out.println(Plane.of(a.pos(),
//                                    d.pos(),
//                                    a.pos().add(a.vel().multiply(5))));
        Plane p;
        p = Plane.of(b.pos(),
                     c.pos(),
                     b.pos().add(b.vel().multiply(5)));
        System.out.println(p);
        System.out.println(p.contains(rock.pos()));
//        p = Plane.of(b.pos(),
//                     c.pos(),
//                     c.pos().add(b.vel().multiply(4)));
//        System.out.println(p);
//        System.out.println(p.contains(rock.pos()));
    }

    @Override
    protected Long solvePartOne(List<Hailstone> hailstones) {
        return solvePartOne(hailstones, 200_000_000_000_000L, 400_000_000_000_000L);
    }

    @Override
    protected Long solvePartTwo(List<Hailstone> hailstones) {
        /*
equal YZ slope:
226614096902854, 205663209347485, 250203858638726 @ 46, 21, -16
339871829605604, 301592523784752, 287903705946757 @ -73, 21, -16

2, 2, 2 @ 4, 2, -1
3, 3, 2 @ -3, 2, -1
         */
        var equations = new Eq[hailstones.size()];
        for (int i = 0; i < hailstones.size(); i++) {
            var s = hailstones.get(i);
            equations[i] = new Eq(i, s.pos().xy(), s.vel().xy(), s.xy());
        }
        for (int i = 0; i < equations.length; i++) {
            var a = equations[i];
            for (int j = i + 1; j < equations.length; j++) {
                var b = equations[j];
                if (a.l().m() == b.l().m()) {
                    System.out.printf("X-Y PARALLEL @ %f: %s and %s%n", b.l().m(), a.i, b.i);
                }
            }
        }
        for (int i = 0; i < hailstones.size(); i++) {
            var s = hailstones.get(i);
            equations[i] = new Eq(i, s.pos().xz(), s.vel().xz(), s.xz());
        }
        for (int i = 0; i < equations.length; i++) {
            var a = equations[i];
            for (int j = i + 1; j < equations.length; j++) {
                var b = equations[j];
                if (a.l().m() == b.l().m()) {
                    System.out.printf("X-Z PARALLEL @ %f: %s and %s%n", b.l().m(), a.i, b.i);
                }
            }
        }
        for (int i = 0; i < hailstones.size(); i++) {
            var s = hailstones.get(i);
            equations[i] = new Eq(i, s.pos().yz(), s.vel().yz(), s.yz());
        }
        for (int i = 0; i < equations.length; i++) {
            var a = equations[i];
            for (int j = i + 1; j < equations.length; j++) {
                var b = equations[j];
                if (a.l().m() == b.l().m()) {
                    System.out.printf("Y-Z PARALLEL @ %f: %s and %s%n", b.l().m(), a.i, b.i);
                }
            }
        }
        return 0L;
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

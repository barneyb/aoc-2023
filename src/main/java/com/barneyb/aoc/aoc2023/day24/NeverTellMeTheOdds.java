package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.geom.Point3;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.List;

public class NeverTellMeTheOdds extends SolvePartOne<List<Hailstone>, Long> {

    public static void main(String[] args) {
        new NeverTellMeTheOdds().solveAndPrint();
    }

    @Override
    protected Long solvePartOne(List<Hailstone> hailstones) {
        return solvePartOne(hailstones, 200_000_000_000_000L, 400_000_000_000_000L);
    }

    @Override
    protected List<Hailstone> buildModel(Input input) {
        return input.streamLines()
                .map(l -> l.split("@"))
                .map(ps -> new Hailstone(Point3.parse(ps[0]),
                                         Point3.parse(ps[1])))
                .toList();
    }

    public Long solvePartOne(List<Hailstone> hailstones, long min, long max) {
        record Eq(Point p, Point v, double m, double b) {}
        var equations = new Eq[hailstones.size()];
        for (int i = 0; i < hailstones.size(); i++) {
            var s = hailstones.get(i);
            double m = (double) s.vel().y() / s.vel().x();
            double tIntercept = (double) -s.pos().x() / s.vel().x();
            var b = s.pos().y() + tIntercept * s.vel().y();
            equations[i] = new Eq(
                    s.pos().xy(),
                    s.vel().xy(),
                    m,
                    b
            );
        }

        long count = 0;
        for (int i = 0; i < equations.length; i++) {
            var a = equations[i];
            for (int j = i + 1; j < equations.length; j++) {
                var b = equations[j];
//                System.out.println(a);
//                System.out.println(b);
                var denom = a.m - b.m;
                if (denom == 0) {
                    // parallel
//                    System.out.println("Hailstones' paths are parallel; they never intersect.");
//                    System.out.println();
                    continue;
                }
                var x = (b.b - a.b) / denom;
                var y = b.m * x + b.b;
                var t1 = (x - a.p.x()) / a.v.x();
                var t2 = (x - b.p.x()) / b.v.x();
                if (t1 < 0) {
//                    if (t2 < 0) {
//                        System.out.printf("Hailstones' paths crossed in the past for both hailstones (t=%f/%f).%n",
//                                          t1,
//                                          t2);
//                    } else {
//                        System.out.printf("Hailstones' paths crossed in the past for hailstone A (t=%f/%f).%n", t1, t2);
//                    }
                } else if (t2 < 0) {
//                    System.out.printf("Hailstones' paths crossed in the past for hailstone B (t=%f/%f).%n", t1, t2);
                } else if (min <= x && x <= max && min <= y && y <= max) {
//                    System.out.printf(
//                            "Hailstones' paths will cross inside the test area (at x=%f, y=%f, t=%f/%f).%n",
//                            x,
//                            y,
//                            t1,
//                            t2);
                    count += 1;
//                } else {
//                    System.out.printf("Hailstones' paths will cross outside the test area (at x=%f, y=%f, t=%f/%f).%n",
//                                      x,
//                                      y, t1, t2);
                }
//                System.out.println();
            }
        }
        return count;
    }

}

package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.geom.Point3;

import static com.barneyb.aoc.aoc2023.day24.Ratio.ONE;
import static com.barneyb.aoc.aoc2023.day24.Ratio.ZERO;

public record Plane(Ratio a, Ratio b, Ratio c, Ratio d) {

    public Plane(long a, long b, long c, long d) {
        this(Ratio.of(a), Ratio.of(b), Ratio.of(c), Ratio.of(d));
    }

    public static Plane of(Point3 p1, Point3 p2, Point3 p3) {
        // equation ax + by + cz + d = 0
        // build matrix
        var A = new Ratio[][]{
                { Ratio.of(p1.y()), Ratio.of(p1.z()), ONE, Ratio.of(-p1.x()), },
                { Ratio.of(p2.y()), Ratio.of(p2.z()), ONE, Ratio.of(-p2.x()), },
                { Ratio.of(p3.y()), Ratio.of(p3.z()), ONE, Ratio.of(-p3.x()), },
        };
        draw(A);
        // get in reduced row echelon form
        for (int i = 0; i < A.length; i++) {
            if (ZERO.equals(A[i][i])) {
                // hopefully the next is better...
                var t = A[i];
                A[i] = A[i + 1];
                A[i + 1] = t;
            }
            // get this row's one squared away
            if (!ONE.equals(A[i][i])) {
                for (int j = A[i].length - 1; j >= 0; j--) {
                    A[i][j] = A[i][j].divide(A[i][i]);
                }
            }
            // zero all other rows
            for (int r = 0; r < A.length; r++) {
                if (r != i && !ZERO.equals(A[r][i])) {
                    for (int j = A[r].length - 1; j >= i; j--) {
                        A[r][j] = A[r][j].subtract(A[i][j].multiply(A[r][i]));
                    }
                }
            }
        }
        draw(A);
        // instantiate
        Ratio ar = ONE;
        Ratio br = A[0][3];
        Ratio cr = A[1][3];
        Ratio dr = A[2][3];
        if (!br.isIntegral() || !cr.isIntegral() || !dr.isIntegral()) {
            long lcm = Factors.lcm(Factors.lcm(br.denom(), cr.denom()), dr.denom());
            ar = ar.multiply(lcm);
            br = br.multiply(lcm);
            cr = cr.multiply(lcm);
            dr = dr.multiply(lcm);
        }
        assert br.isIntegral() && cr.isIntegral() && dr.isIntegral();
        return new Plane(ar.num(), br.num(), cr.num(), dr.num());
    }

    public boolean contains(Point3 p) {
        return a.multiply(p.x())
                .add(b.multiply(p.y()))
                .add(c.multiply(p.z()))
                .add(d)
                .equals(ZERO);
    }

    private static void draw(Ratio[][] A) {
        var widths = new int[A[0].length];
        for (var row : A) {
            for (int j = 0; j < row.length; j++) {
                widths[j] = Math.max(widths[j], row[j].toString().length());
            }
        }
        for (var row : A) {
            for (int j = 0; j < row.length; j++) {
                var s = row[j].toString();
                System.out.printf("%s ", " ".repeat(widths[j] - s.length()) + s);
            }
            System.out.println();
        }
        System.out.println();
    }

}

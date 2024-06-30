package com.barneyb.aoc.aoc2023.day24;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.WeakHashMap;

public class Factors {

    private static final Map<Long, List<Long>> FACTORS = new WeakHashMap<>();

    public static List<Long> of(long n) {
        n = Math.abs(n);
        return FACTORS.computeIfAbsent(n, Factors::computeFactors);
    }

    private static List<Long> computeFactors(long n) {
        if (n == 1) return List.of(1L);
        List<Long> lo = new ArrayList<>();
        lo.add(1L);
        List<Long> hi = new ArrayList<>();
        hi.add(n);
        long max = (long) Math.sqrt((double) n);
        for (long f = 2; f < max; f++) {
            if (n % f == 0) {
                lo.add(f);
                hi.add(n / f);
            }
        }
        if (n % max == 0) {
            // squares only need their root once
            lo.add(max);
        }
        Collections.reverse(hi);
        lo.addAll(hi);
        return List.copyOf(lo);
    }

    public static List<Long> common(long n, long m) {
        var result = new ArrayList<Long>();
        var aItr = of(n).iterator();
        var a = aItr.next();
        var bItr = of(m).iterator();
        var b = bItr.next();
        while (aItr.hasNext() && bItr.hasNext()) {
            if (a.equals(b)) {
                result.add(a);
                a = aItr.next();
                b = bItr.next();
            } else if (a.compareTo(b) < 0) {
                a = aItr.next();
            } else { // b is less
                b = bItr.next();
            }
        }
        return result;
    }

    public static long gcd(long n, long m) {
        n = Math.abs(n);
        m = Math.abs(m);
        long t;
        // Euclid's algorithm
        while (m != 0) {
            t = m;
            m = n % m;
            n = t;
        }
        return n;
    }

    public static long lcm(long n, long m) {
        n = Math.abs(n);
        m = Math.abs(m);
        return n * m / gcd(n, m);
    }

}

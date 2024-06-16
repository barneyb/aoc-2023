package com.barneyb.aoc.aoc2023.day24;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class FactorsTest {

    @Test
    void of() {
        // prime
        assertEquals(ll(1, 7), Factors.of(7));
        // just square
        assertEquals(ll(1, 5, 25), Factors.of(25));
        // square and more
        assertEquals(ll(1, 2, 3, 4, 6, 9, 12, 18, 36), Factors.of(36));
        // non-square negative
        assertEquals(ll(1, 3, 5, 7, 9, 15, 21, 35, 45, 63, 105, 315), Factors.of(-315));
    }

    @Test
    void common() {
        assertEquals(ll(1, 3, 5, 9, 15, 45), Factors.common(315, 13140));
        assertEquals(ll(1), Factors.common(9, 10));
        assertEquals(ll(1), Factors.common(5, 7));
    }

    @Test
    void gcd() {
        assertEquals(45L, Factors.gcd(315, 13140));
        assertEquals(1, Factors.gcd(9, 10));
        assertEquals(1, Factors.gcd(5, 7));
    }

    @Test
    void lcm() {
        assertEquals(35L, Factors.lcm(5, 7));
        assertEquals(24L, Factors.lcm(6, 8));
    }

    private List<Long> ll(int... ns) {
        ArrayList<Long> longs = new ArrayList<>(ns.length);
        for (var n : ns) longs.add((long) n);
        return longs;
    }

}

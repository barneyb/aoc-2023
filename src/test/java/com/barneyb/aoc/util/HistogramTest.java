package com.barneyb.aoc.util;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class HistogramTest {

    @Test
    void count_single() {
        var h = new Histogram<Integer>();
        h.count(1);
        h.count(1);
        h.count(2);
        assertEquals(2, h.size());
        assertEquals(2, h.get(1));
        assertEquals(1, h.get(2));
    }

    @Test
    void count_multiple() {
        var h = new Histogram<Integer>();
        h.count(1, 3);
        h.count(1, 7);
        assertEquals(10, h.get(1));
    }

    @Test
    void buckets() {
        var h = new Histogram<Integer>();
        assertTrue(h.buckets().isEmpty());
        h.count(1);
        assertEquals(Collections.singleton(1), h.buckets());
        h.count(2);
        assertEquals(new HashSet<>(Arrays.asList(1, 2)), h.buckets());
    }

    @Test
    void buckets_filtered() {
        var h = new Histogram<Integer>();
        h.count(1, 1);
        h.count(2, 10);
        h.count(3, 10);
        h.count(4, 1);
        assertEquals(new HashSet<>(Arrays.asList(2, 3)),
                     h.buckets(c -> c > 1));
    }

}

package com.barneyb.aoc.util;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

class RangeTest {

    @Test
    void size() {
        assertEquals(1, new Range(0, 0).size());
        assertEquals(3, new Range(0, 2).size());
        assertEquals(3, new Range(0, -2).size());
    }

    @Test
    void iterator_up() {
        var itr = new Range(0, 2).iterator();
        assertEquals(0, itr.next());
        assertEquals(1, itr.next());
        assertEquals(2, itr.next());
        assertFalse(itr.hasNext());
    }

    @Test
    void iterator_down() {
        var itr = new Range(0, -2).iterator();
        assertEquals(0, itr.next());
        assertEquals(-1, itr.next());
        assertEquals(-2, itr.next());
        assertFalse(itr.hasNext());
    }

}

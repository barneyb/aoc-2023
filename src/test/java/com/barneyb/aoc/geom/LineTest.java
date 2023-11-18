package com.barneyb.aoc.geom;

import com.barneyb.aoc.util.Range;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LineTest {

    private final Line vert = new Line(
            new Point(0, 0),
            new Point(0, 2));
    private final Line horiz = new Line(
            new Point(1, 0),
            new Point(-1, 0));

    @Test
    void isVertical() {
        assertTrue(vert.isVertical());
        assertFalse(horiz.isVertical());
    }

    @Test
    void isHorizontal() {
        assertFalse(vert.isHorizontal());
        assertTrue(horiz.isHorizontal());
    }

    @Test
    void xRange() {
        assertEquals(new Range(1, -1),
                     horiz.xRange());
    }

    @Test
    void yRange() {
        assertEquals(new Range(0, 2),
                     vert.yRange());
    }

    @Test
    void points_vertical() {
        var itr = vert.points();
        assertEquals(new Point(0, 0), itr.next());
        assertEquals(new Point(0, 1), itr.next());
        assertEquals(new Point(0, 2), itr.next());
        assertFalse(itr.hasNext());
    }

    @Test
    void points_horizontal() {
        var itr = horiz.points();
        assertEquals(new Point(1, 0), itr.next());
        assertEquals(new Point(0, 0), itr.next());
        assertEquals(new Point(-1, 0), itr.next());
        assertFalse(itr.hasNext());
    }

}

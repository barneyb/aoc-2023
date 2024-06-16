package com.barneyb.aoc.aoc2023.day24;

import com.barneyb.aoc.geom.Point3;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class PlaneTest {

    @Test
    void ofPoints() {
        assertEquals(new Plane(1L, 3L, 4L, -9L),
                     Plane.of(Point3.of(1, 0, 2),
                              Point3.of(2, 1, 1),
                              Point3.of(-1, 2, 1)));
    }

}

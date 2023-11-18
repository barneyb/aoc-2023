package com.barneyb.aoc.aoc2021.day05;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class HydrothermalVentureTest {

    @Test
    void parse() {
        var lines = new HydrothermalVenture()
                .buildModel(Input.of("7,0 -> 3,4"));
        assertEquals(1, lines.size());
        var l = lines.get(0);
        assertEquals(new Point(7, 0), l.a());
        assertEquals(new Point(3, 4), l.b());
    }

    @Test
    void realWorld() {
        new HydrothermalVenture().test(7644);
    }

}

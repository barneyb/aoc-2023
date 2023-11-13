package com.barneyb.aoc.aoc2016.day02;

import com.barneyb.aoc.geom.Dir;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class BathroomSecurityTest {

    @Test
    void exampleOne() {
        Input in = Input.of("""
                                    ULL
                                    RRDDD
                                    LURDL
                                    UUUUD""");

        BathroomSecurity bathSec = new BathroomSecurity();
        List<List<Dir>> rows = bathSec.buildModel(in);

        assertEquals(List.of(
                List.of(Dir.NORTH, Dir.WEST, Dir.WEST),
                List.of(Dir.EAST, Dir.EAST, Dir.SOUTH, Dir.SOUTH, Dir.SOUTH),
                List.of(Dir.WEST, Dir.NORTH, Dir.EAST, Dir.SOUTH, Dir.WEST),
                List.of(Dir.NORTH, Dir.NORTH, Dir.NORTH, Dir.NORTH, Dir.SOUTH)
        ), rows);

        String code = bathSec.solvePartOne(rows);

        assertEquals("1985", code);
    }

    @Test
    void partOne() {
        new BathroomSecurity().test("61529");
    }

}

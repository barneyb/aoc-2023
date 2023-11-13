package com.barneyb.aoc.aoc2016.day02;

import com.barneyb.aoc.geom.Dir;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class BathroomSecurityTest {

    public static final String EXAMPLE_INPUT = """
            ULL
            RRDDD
            LURDL
            UUUUD""";

    @Test
    void exampleOne() {
        Input in = Input.of(EXAMPLE_INPUT);
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
    void realWorld() {
        new BathroomSecurity().test("61529",
                                    "C2C28");
    }

    @Test
    void exampleTwo() {
        Input in = Input.of(EXAMPLE_INPUT);
        BathroomSecurity bathSec = new BathroomSecurity();
        List<List<Dir>> rows = bathSec.buildModel(in);

        String code = bathSec.solvePartTwo(rows);

        assertEquals("5DB3", code);
    }

}

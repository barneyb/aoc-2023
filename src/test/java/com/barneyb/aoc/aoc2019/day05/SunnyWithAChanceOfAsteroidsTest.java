package com.barneyb.aoc.aoc2019.day05;

import com.barneyb.aoc.aoc2019.day02.Intcode;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SunnyWithAChanceOfAsteroidsTest {

    @Test
    void realWorld() {
        new SunnyWithAChanceOfAsteroids()
                .test(13978427, 11189491);
    }

    @Test
    void exampleTwo() {
        var prog = Intcode.parse(Input.of(
                """
                        3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""));
        var out = new ArrayList<Integer>();
        new Intcode(prog, () -> 7, out::add).run();
        new Intcode(prog, () -> 8, out::add).run();
        new Intcode(prog, () -> 9, out::add).run();
        assertEquals(List.of(999, 1000, 1001), out);
    }

}

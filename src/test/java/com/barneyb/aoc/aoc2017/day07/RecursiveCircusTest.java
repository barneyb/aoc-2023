package com.barneyb.aoc.aoc2017.day07;

import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;

class RecursiveCircusTest {

    private static final String EXAMPLE_ONE = """
            pbga (66)
            xhth (57)
            ebii (61)
            havc (66)
            ktlj (57)
            fwft (72) -> ktlj, cntj, xhth
            qoyq (66)
            padx (45) -> pbga, havc, qoyq
            tknk (41) -> ugml, padx, fwft
            jptl (61)
            ugml (68) -> gyxo, ebii, jptl
            gyxo (61)
            cntj (57)""";

    @Test
    void buildModel() {
        var progs = new RecursiveCircus().buildModel(
                Input.of(EXAMPLE_ONE));

        assertEquals(13, progs.size());
        assertEquals("pbga", progs.get(0).name());
        assertEquals(61, progs.get(2).weight());
        assertEquals(Set.of(), progs.get(4).above());
        assertEquals(Set.of("pbga", "havc", "qoyq"), progs.get(7).above());
    }

    @Test
    void exampleOne() {
        var solver = new RecursiveCircus();
        assertEquals("tknk",
                     solver.solvePartOne(
                             solver.buildModel(
                                     Input.of(EXAMPLE_ONE))));
    }

    @Test
    void realWorld() {
        new RecursiveCircus().test("hlhomy");
    }

}

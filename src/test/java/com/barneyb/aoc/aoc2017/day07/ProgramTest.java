package com.barneyb.aoc.aoc2017.day07;

import org.junit.jupiter.api.Test;

import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class ProgramTest {

    @Test
    void parse_branch() {
        var prog = Program.parse("fwft (72) -> ktlj, cntj, xhth");
        assertEquals("fwft", prog.name());
        assertEquals(72, prog.weight());
        assertEquals(Set.of("ktlj", "cntj", "xhth"), prog.above());
        assertFalse(prog.isLeaf());
    }

    @Test
    void parse_leaf() {
        var prog = Program.parse("ebii (61)");
        assertEquals("ebii", prog.name());
        assertEquals(61, prog.weight());
        assertEquals(Set.of(), prog.above());
        assertTrue(prog.isLeaf());
    }

}

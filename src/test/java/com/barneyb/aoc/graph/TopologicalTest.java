package com.barneyb.aoc.graph;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.fail;

class TopologicalTest {

    Digraph<Integer> diamond;

    @BeforeEach
    void setUp() {
        diamond = new Digraph<>();
        diamond.addEdge(2, 4);
        diamond.addEdge(1, 3);
        diamond.addEdge(3, 4);
        diamond.addEdge(1, 2);
    }

    @Test
    void diamond() {
        var itr = new Topological<>(diamond)
                .iterator();
        assertEquals(1, itr.next());
        switch (itr.next()) {
            case 2 -> assertEquals(3, itr.next());
            case 3 -> assertEquals(2, itr.next());
            default -> fail("got neither 2 nor 3");
        }
        assertEquals(4, itr.next());
        assertFalse(itr.hasNext(), "had more, but shouldn't have");
    }

    @Test
    void reverse() {
        var itr = new Topological<>(diamond)
                .reverse()
                .iterator();
        assertEquals(4, itr.next());
        switch (itr.next()) {
            case 2 -> assertEquals(3, itr.next());
            case 3 -> assertEquals(2, itr.next());
            default -> fail("got neither 2 nor 3");
        }
        assertEquals(1, itr.next());
        assertFalse(itr.hasNext(), "had more, but shouldn't have");
    }

}

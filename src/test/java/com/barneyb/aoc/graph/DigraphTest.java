package com.barneyb.aoc.graph;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class DigraphTest {

    private Digraph<Integer> diamond;

    @BeforeEach
    void setUp() {
        diamond = new Digraph<>();
        diamond.addEdge(1, 2);
        diamond.addEdge(1, 3);
        diamond.addEdge(2, 4);
        diamond.addEdge(3, 4);
    }

    @Test
    void size() {
        assertEquals(4, diamond.size());
    }

    @Test
    void vertices() {
        Set<Integer> vs = new HashSet<>();
        for (Integer v : diamond.vertices()) {
            assertTrue(vs.add(v), "Duplicate " + v);
        }
        assertEquals(diamond.size(), vs.size());
        for (int i = diamond.size(); i > 0; i--) {
            assertTrue(vs.contains(i), "Didn't find " + i);
        }
    }

    @Test
    void adjacent() {
        assertEquals(List.of(2, 3), diamond.adjacent(1));
        assertEquals(List.of(4), diamond.adjacent(2));
        assertEquals(List.of(4), diamond.adjacent(3));
        assertEquals(List.of(), diamond.adjacent(4));
    }

}

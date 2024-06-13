package com.barneyb.aoc.graph;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import static java.util.Collections.emptyList;

/**
 * Adjacency list graph structure. Parallel and self edges are allowed.
 *
 * @param <V> node data
 */
public class Digraph<V> {

    private final Map<V, Collection<V>> adjacent = new HashMap<>();

    /**
     * Add a new edge to the graph.
     */
    public void addEdge(V from, V to) {
        adjacent.computeIfAbsent(to, k -> new ArrayList<>());
        adjacent.computeIfAbsent(from, k -> new ArrayList<>())
                .add(to);
    }

    public int size() {
        return adjacent.size();
    }

    public Set<V> vertices() {
        return adjacent.keySet();
    }

    /**
     * Return the vertices adjacent to the passed vertex.
     */
    public Iterable<V> adjacent(V v) {
        return adjacent.getOrDefault(v, emptyList());
    }

}

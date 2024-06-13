package com.barneyb.aoc.graph;

import java.util.Set;

public class Graph<V> {

    private final Digraph<V> delegate = new Digraph<>();

    /**
     * Add a new edge to the graph.
     */
    public void addEdge(V from, V to) {
        delegate.addEdge(from, to);
        delegate.addEdge(to, from);
    }

    public int size() {
        return delegate.size();
    }

    public Set<V> vertices() {
        return delegate.vertices();
    }

    /**
     * Return the vertices adjacent to the passed vertex.
     */
    public Iterable<V> adjacent(V v) {
        return delegate.adjacent(v);
    }

}

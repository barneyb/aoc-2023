package com.barneyb.aoc.graph;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

/**
 * Finds a topological order for a {@link Digraph}. No check is made for cycles
 * in the graph. If a cyclic graph is passed, the result is undefined.
 */
public class Topological<V> implements Iterable<V> {

    private final Set<V> visited;
    /**
     * Stores the sorted order. Use a Deque (as a stack) to collect the
     * postorder AND reverse it at the same time.
     */
    private final Deque<V> order;
    private List<V> reverse;

    public Topological(Digraph<V> graph) {
        visited = new HashSet<>(graph.size());
        order = new ArrayDeque<>(graph.size());
        for (V v : graph.vertices())
            if (!visited.contains(v))
                dfs(graph, v);
    }

    private void dfs(Digraph<V> graph, V v) {
        visited.add(v);
        for (V w : graph.adjacent(v))
            if (!visited.contains(w))
                dfs(graph, w);
        order.addFirst(v);
    }

    @Override
    public Iterator<V> iterator() {
        return order.iterator();
    }

    public Iterable<V> reverse() {
        if (reverse == null) {
            List<V> list = new ArrayList<>(order);
            Collections.reverse(list);
            reverse = list;
        }
        return reverse;
    }

}

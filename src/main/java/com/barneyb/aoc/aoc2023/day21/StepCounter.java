package com.barneyb.aoc.aoc2023.day21;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.graph.Graph;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class StepCounter extends SolvePartOne<StepCounter.Model, Long> {

    private static final char START = 'S';
    private static final char ROCK = '#';

    public static void main(String[] args) {
        new StepCounter().solveAndPrint();
    }

    @Override
    protected Long solvePartOne(Model model) {
        return solvePartOne(model, 64);
    }

    protected Long solvePartOne(Model model, int steps) {
        Set<Point> curr = Collections.singleton(model.start());
        for (int i = 0; i < steps; i++) {
            Set<Point> next = new HashSet<>();
            for (Point p : curr)
                for (Point a : model.graph().adjacent(p))
                    next.add(a);
            curr = next;
        }
        return (long) curr.size();
    }

    @Override
    protected Model buildModel(Input input) {
        Point start = null;
        Graph<Point> graph = new Graph<>();
        int y = 0;
        char[] lineNorth = null;
        for (String lineStr : input) {
            var line = lineStr.toCharArray();
            int x = 0;
            char west = ROCK;
            for (char c : line) {
                if (c != ROCK) {
                    Point p = new Point(x, y);
                    if (c == START) start = p;
                    char north = lineNorth == null ? ROCK : lineNorth[x];
                    if (north != ROCK) graph.addEdge(p, new Point(x, y - 1));
                    if (west != ROCK) graph.addEdge(p, new Point(x - 1, y));
                }
                x++;
                west = c;
            }
            y++;
            lineNorth = line;
        }
        return new Model(start, graph);
    }

    public record Model(Point start, Graph<Point> graph) {}

}

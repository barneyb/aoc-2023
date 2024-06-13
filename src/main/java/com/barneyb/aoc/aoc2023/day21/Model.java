package com.barneyb.aoc.aoc2023.day21;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.graph.Graph;
import com.barneyb.aoc.util.Input;

public record Model(Point start, int half, int max, Graph<Point> graph) {

    private static final char START = 'S';
    private static final char ROCK = '#';

    static Model from(Input input) {
        Point start = null;
        Graph<Point> graph = new Graph<>();
        int y = 0;
        int x = -1;
        char[] lineNorth = null;
        for (String lineStr : input) {
            var line = lineStr.toCharArray();
            x = 0;
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
        assert x == y : "Non-square garden?!";
        assert x % 2 == 1 : "Width isn't odd?!";
        int max = x - 1;
        int half = max / 2;
        assert Point.of(half, half).equals(start);
        return new Model(start, half, max, graph);
    }

    public Stats<Point> points() {
        return new Stats<>(
                Point.of(half, half),
                Point.of(half, 0),
                Point.of(half, max),
                Point.of(max, half),
                Point.of(0, half),
                Point.of(max, 0),
                Point.of(0, 0),
                Point.of(max, max),
                Point.of(0, max)
        );
    }

    int dim() {
        return max + 1;
    }

    Model startAt(Point start) {
        return new Model(start, half, max, graph);
    }

}

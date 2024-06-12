package com.barneyb.aoc.aoc2023.day21;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.graph.Graph;
import com.barneyb.aoc.util.Input;

public record Model(Point start, int width, int height, Graph<Point> graph) {

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
        assert x % 2 == 1 : "Width isn't odd?!";
        assert y % 2 == 1 : "Height isn't odd?!";
        return new Model(start, x, y, graph);
    }

    Model startAt(Point start) {
        return new Model(start, width, height, graph);
    }

}

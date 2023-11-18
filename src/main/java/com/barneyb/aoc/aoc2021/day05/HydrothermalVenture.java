package com.barneyb.aoc.aoc2021.day05;

import com.barneyb.aoc.geom.Line;
import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Histogram;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.ArrayList;
import java.util.List;

public class HydrothermalVenture extends SolvePartOne<List<Line>, Integer> {

    public static void main(String[] args) {
        new HydrothermalVenture().solveAndPrint();
    }

    @Override
    protected List<Line> buildModel(Input input) {
        List<Line> lines = new ArrayList<>();
        for (String l : input) {
            var coords = l.split(" -> ");
            lines.add(new Line(Point.parse(coords[0]),
                               Point.parse(coords[1])));
        }
        return lines;
    }

    @Override
    protected Integer solvePartOne(List<Line> lines) {
        Histogram<Point> hist = new Histogram<>();
        lines.stream()
                .filter(l -> l.isHorizontal() || l.isVertical())
                .forEach(line -> line.points().forEachRemaining(hist::count));
        return hist.buckets(c -> c > 1)
                .size();
    }

}

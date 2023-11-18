package com.barneyb.aoc.aoc2021.day05;

import com.barneyb.aoc.geom.Line;
import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Answers;
import com.barneyb.aoc.util.Histogram;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveTogether;

import java.util.ArrayList;
import java.util.List;

public class HydrothermalVenture extends SolveTogether<List<Line>, Integer, Integer> {

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
    protected Answers<Integer, Integer> solveTogether(List<Line> lines) {
        Histogram<Point> histOne = new Histogram<>();
        Histogram<Point> histTwo = new Histogram<>();
        lines.forEach(line -> {
            boolean rect = line.isHorizontal() || line.isVertical();
            line.points().forEachRemaining(p -> {
                if (rect) histOne.count(p);
                histTwo.count(p);
            });
        });
        return new Answers<>(
                histOne.buckets(c -> c > 1).size(),
                histTwo.buckets(c -> c > 1).size());
    }

}

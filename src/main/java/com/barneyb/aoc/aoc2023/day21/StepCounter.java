package com.barneyb.aoc.aoc2023.day21;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class StepCounter extends SolveEachPart<Model, Long, Long> {

    public static void main(String[] args) {
        new StepCounter().solveAndPrint();
    }

    @Override
    protected Long solvePartOne(Model model) {
        return solvePartOne(model, 64);
    }

    protected Long solvePartOne(Model model, int steps) {
        return buildTrace(model).get(steps);
    }

    protected List<Long> buildTrace(Model model) {
        var trace = new ArrayList<Long>();
        Set<Point> curr = Collections.singleton(model.start());
        while (true) {
            trace.add((long) curr.size());
            // are we done?
            var l = trace.size();
            if (l > 5
                && trace.get(l - 1).equals(trace.get(l - 3))
                && trace.get(l - 1).equals(trace.get(l - 5))) {
                break;
            }
            curr = tick(model, curr);
        }
        return trace;
    }

    private static Set<Point> tick(Model model, Set<Point> curr) {
        Set<Point> next = new HashSet<>();
        for (Point p : curr)
            for (Point a : model.graph().adjacent(p))
                next.add(a);
        curr = next;
        return curr;
    }

    @Override
    protected Long solvePartTwo(Model model) {
        return solvePartTwo(model, 26501365);
    }

    protected Long solvePartTwo(Model model, int steps) {
        assert model.width() == model.height() : "Non-square garden?!";
        int max = model.width() - 1;
        int half = max / 2;
        assert model.start().equals(Point.of(half, half));
        var p = new Stats<>(
                model.start(),
                Point.of(half, 0),
                Point.of(half, max),
                Point.of(max, half),
                Point.of(0, half),
                Point.of(max, 0),
                Point.of(0, 0),
                Point.of(max, max),
                Point.of(0, max)
        );
        var trace = new Stats<>(
                buildTrace(model),
                buildTrace(model.startAt(p.north)),
                buildTrace(model.startAt(p.east)),
                buildTrace(model.startAt(p.west)),
                buildTrace(model.startAt(p.south)),
                buildTrace(model.startAt(p.northwest)),
                buildTrace(model.startAt(p.northeast)),
                buildTrace(model.startAt(p.southwest)),
                buildTrace(model.startAt(p.southeast))
        );
        var reach = new Stats<Integer>();
        Set<Point> curr = Collections.singleton(model.start());
        for (int i = 0; !reach.isComplete(); i++) {
            if (reach.center == null && curr.contains(p.center)) reach.center = i;
            if (reach.north == null && curr.contains(p.north)) reach.north = i;
            if (reach.east == null && curr.contains(p.east)) reach.east = i;
            if (reach.west == null && curr.contains(p.west)) reach.west = i;
            if (reach.south == null && curr.contains(p.south)) reach.south = i;
            if (reach.northwest == null && curr.contains(p.northwest)) reach.northwest = i;
            if (reach.northeast == null && curr.contains(p.northeast)) reach.northeast = i;
            if (reach.southwest == null && curr.contains(p.southwest)) reach.southwest = i;
            if (reach.southeast == null && curr.contains(p.southeast)) reach.southeast = i;
            curr = tick(model, curr);
        }
        System.out.println(reach);
        return 0L;
    }

    @Override
    protected Model buildModel(Input input) {
        return Model.from(input);
    }

}

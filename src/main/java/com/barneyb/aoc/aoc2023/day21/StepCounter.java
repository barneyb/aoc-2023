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
        return (long) buildTrace(model).get(steps).size();
    }

    protected List<Set<Point>> buildTrace(Model model) {
        var trace = new ArrayList<Set<Point>>();
        Set<Point> curr = Collections.singleton(model.start());
        while (true) {
            trace.add(curr);
            // are we done?
            var l = trace.size();
            if (l > model.dim() && trace.get(l - 1).equals(trace.get(l - 3))) {
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
        return solvePartTwo(model, 26_501_365);
    }

    protected Long solvePartTwo(Model model, int steps) {
        var p = model.points();
        var trace = new Stats<>(
                buildTrace(model),
                buildTrace(model.startAt(p.north)),
                buildTrace(model.startAt(p.south)),
                buildTrace(model.startAt(p.east)),
                buildTrace(model.startAt(p.west)),
                buildTrace(model.startAt(p.northeast)),
                buildTrace(model.startAt(p.northwest)),
                buildTrace(model.startAt(p.southeast)),
                buildTrace(model.startAt(p.southwest))
        );
        var reach = new Stats<>(
                0,
                model.half() + 1,
                model.half() + 1,
                model.half() + 1,
                model.half() + 1,
                model.dim() + 1,
                model.dim() + 1,
                model.dim() + 1,
                model.dim() + 1
        );
        return getResult(model, steps, reach, trace);
    }

    private long getResult(Model model, int steps, Stats<Integer> reach, Stats<List<Set<Point>>> trace) {
        long result = doPartial(steps - reach.center, trace.center);
        result += doCardinal(model, steps - reach.west, trace.east);
        result += doCardinal(model, steps - reach.east, trace.west);
        result += doCardinal(model, steps - reach.north, trace.south);
        result += doCardinal(model, steps - reach.south, trace.north);
        result += doQuadrant(model, steps - reach.northeast, trace.southwest);
        result += doQuadrant(model, steps - reach.northwest, trace.southeast);
        result += doQuadrant(model, steps - reach.southeast, trace.northwest);
        result += doQuadrant(model, steps - reach.southwest, trace.northeast);
        return result;
    }

    private long doPartial(int steps, List<Set<Point>> trace) {
        if (steps < 0) return 0;
        if (steps >= trace.size()) {
            var excess = steps - trace.size();
            steps = trace.size() - (excess % 2 == 0 ? 2 : 1);
        }
        return trace.get(steps).size();
    }

    private long doCardinal(Model model, int steps, List<Set<Point>> trace) {
        int period = model.dim();
        long result = 0;
        int cycles = steps / (period << 1);
        if (cycles > 1) {
            cycles -= 1; // last cycle is special
            int l = trace.size();
            int odds = trace.get(l - 1).size();
            int evens = trace.get(l - 2).size();
            result += (long) cycles * (odds + evens);
            steps -= cycles * period << 1;
        }
        while (steps >= 0) {
            result += doPartial(steps, trace);
            steps -= period;
        }
        return result;
    }

    private long doQuadrant(Model model, int steps, List<Set<Point>> trace) {
        int period = model.dim();
        long result = 0;
        int count = 1;
        int cycles = steps / (period << 1);
        if (cycles > 1) {
            cycles -= 1; // last cycle is special
            var fulls = cycles * 2;
            int l = trace.size();
            int odds = trace.get(l - 1).size();
            int evens = trace.get(l - 2).size();
            long no = halftone_triangle(fulls - steps % 2);
            long ne = halftone_triangle(fulls - (steps - 1) % 2);
            result += no * odds
                      + ne * evens;
            steps -= fulls * period;
            count += fulls;
        }
        while (steps >= 0) {
            result += count * doPartial(steps, trace);
            steps -= period;
            count += 1;
        }
        return result;
    }

    static long triangle(long n) {
        return n * (n + 1) / 2;
    }

    static long halftone_triangle(long n) {
        var h = n / 2;
        var hprime = n - h;
        return triangle(h) + triangle(hprime);
    }

    @Override
    protected Model buildModel(Input input) {
        return Model.from(input);
    }

}

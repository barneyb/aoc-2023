package com.barneyb.aoc.aoc2016.day01;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class NoTimeForATaxicab extends SolveEachPart<List<Step>, Long, Long> {

    public static void main(String[] args) {
        new NoTimeForATaxicab().solveAndPrint();
    }

    protected NoTimeForATaxicab() {
        super(2016, 1);
    }

    @Override
    protected List<Step> buildModel(Input input) {
        List<Step> steps = new ArrayList<>();
        for (String line : input.firstLine().split(",\\s*")) {
            steps.add(Step.parse(line));
        }
        return steps;
    }

    @Override
    protected Long solvePartOne(List<Step> steps) {
        State pos = State.ORIGIN;
        for (Step s : steps) {
            pos = pos.move(s);
        }
        return pos.manhattanDistance();
    }

    @Override
    protected Long solvePartTwo(List<Step> steps) {
        State state = State.ORIGIN;
        Set<Point> visited = new HashSet<>();
        for (Step s : steps) {
            state = state.turn(s.turn());
            for (Long i = s.distance(); i > 0; i--) {
                state = state.move(1L);
                if (!visited.add(state.position())) {
                    return state.manhattanDistance();
                }
            }
        }
        throw new RuntimeException("Reached no position twice");
    }

}

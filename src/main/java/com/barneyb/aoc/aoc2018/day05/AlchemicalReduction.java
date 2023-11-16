package com.barneyb.aoc.aoc2018.day05;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/*
 * This looks like it ought to be @ConsumesModel, but passing the result of part
 * one's reduction into part two avoids a bunch of re-reducing. If part one can
 * remove a pair of units, they'll be removed in part two anyway, either because
 * they're of the type being removed, or because the part one rules still apply.
 */
public class AlchemicalReduction extends SolveEachPart<List<Unit>, Integer, Integer> {

    public static void main(String[] args) {
        new AlchemicalReduction().solveAndPrint();
    }

    @Override
    protected List<Unit> buildModel(Input input) {
        List<Unit> polymer = new ArrayList<>();
        for (char c : input.toCharArray()) {
            polymer.add(Unit.of(c));
        }
        return polymer;
    }

    @Override
    protected Integer solvePartOne(List<Unit> polymer) {
        for (int i = polymer.size() - 2; i >= 0; i--) {
            if (polymer.get(i).isReactive(polymer.get(i + 1))) {
                polymer.remove(i);
                polymer.remove(i);
                if (i == polymer.size()) i--;
            }
        }
        return polymer.size();
    }

    @Override
    protected Integer solvePartTwo(List<Unit> polymer) {
        Set<Character> types = new HashSet<>();
        for (Unit u : polymer) types.add(u.type());
        int best = polymer.size();
        for (Character type : types) {
            List<Unit> stripped = new ArrayList<>(polymer);
            stripped.removeIf(u -> u.type() == type);
            best = Math.min(best,
                            solvePartOne(stripped));
        }
        return best;
    }

}

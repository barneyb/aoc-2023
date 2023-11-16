package com.barneyb.aoc.aoc2018.day05;

import com.barneyb.aoc.util.ConsumesModel;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.ArrayList;
import java.util.List;

@ConsumesModel
public class AlchemicalReduction extends SolvePartOne<List<Unit>, Integer> {

    public static void main(String[] args) {
        new AlchemicalReduction().solveAndPrint();
    }

    @Override
    protected List<Unit> buildModel(Input input) {
        List<Unit> units = new ArrayList<>();
        for (char c : input.toCharArray()) {
            units.add(Unit.of(c));
        }
        return units;
    }

    @Override
    protected Integer solvePartOne(List<Unit> units) {
        for (int i = units.size() - 2; i >= 0; i--) {
            if (units.get(i).isReactive(units.get(i + 1))) {
                units.remove(i);
                units.remove(i);
            }
        }
        return units.size();
    }

}

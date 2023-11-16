package com.barneyb.aoc.aoc2019.day05;

import com.barneyb.aoc.aoc2019.day02.Intcode;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.ArrayList;
import java.util.List;

public class SunnyWithAChanceOfAsteroids extends SolvePartOne<int[], Integer> {

    public static void main(String[] args) {
        new SunnyWithAChanceOfAsteroids()
                .solveAndPrint();
    }

    @Override
    protected int[] buildModel(Input input) {
        return Intcode.parse(input);
    }

    @Override
    protected Integer solvePartOne(int[] program) {
        List<Integer> codes = new ArrayList<>();
        var vm = new Intcode(program,
                             () -> 1,
                             codes::add);
        vm.run();
        return codes.get(codes.size() - 1);
    }

}

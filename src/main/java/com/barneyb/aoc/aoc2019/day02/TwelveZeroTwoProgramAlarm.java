package com.barneyb.aoc.aoc2019.day02;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

public class TwelveZeroTwoProgramAlarm extends SolveEachPart<int[], Integer, Integer> {

    public static void main(String[] args) {
        new TwelveZeroTwoProgramAlarm()
                .solveAndPrint();
    }

    @Override
    protected int[] buildModel(Input input) {
        return Intcode.parse(input);
    }

    @Override
    protected Integer solvePartOne(int[] program) {
        return compute(program, 12, 2);
    }

    private int compute(int[] program, int noun, int verb) {
        var vm = new Intcode(program);
        vm.write(1, noun);
        vm.write(2, verb);
        vm.run();
        return vm.read(0);
    }

    @Override
    protected Integer solvePartTwo(int[] program) {
        for (int n = 0; n < 100; n++)
            for (int v = 0; v < 100; v++)
                if (compute(program, n, v) == 19690720)
                    return n * 100 + v;
        throw new RuntimeException("Failed to find answer");
    }

}

package com.barneyb.aoc.aoc2019.day02;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

public class TwelveZeroTwoProgramAlarm extends SolvePartOne<int[], Integer> {

    public static void main(String[] args) {
        new TwelveZeroTwoProgramAlarm()
                .solveAndPrint();
    }

    @Override
    protected int[] buildModel(Input input) {
        var source = input.toString()
                .split(",");
        var program = new int[source.length];
        for (int i = 0; i < source.length; i++) {
            String s = source[i];
            program[i] = Integer.parseInt(s);
        }
        return program;
    }

    @Override
    protected Integer solvePartOne(int[] program) {
        var vm = new Intcode(program);
        vm.setPosition(1, 12);
        vm.setPosition(2, 2);
        vm.run();
        return vm.getPosition(0);
    }

}

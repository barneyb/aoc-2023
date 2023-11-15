package com.barneyb.aoc.aoc2017.day05;

import com.barneyb.aoc.util.ConsumesModel;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;

@ConsumesModel
public class AMazeOfTwistyTrampolinesAllAlike extends SolveEachPart<int[], Integer, Integer> {

    public static void main(String[] args) {
        new AMazeOfTwistyTrampolinesAllAlike().solveAndPrint();
    }

    @Override
    protected int[] buildModel(Input input) {
        ArrayList<Integer> list = new ArrayList<>();
        for (String s : input) {
            list.add(Integer.valueOf(s));
        }
        int[] arr = new int[list.size()];
        int i = 0;
        for (int j : list) {
            arr[i++] = j;
        }
        return arr;
    }

    @Override
    protected Integer solvePartOne(int[] jumps) {
        int idx = 0;
        int steps = 0;
        while (idx >= 0 && idx < jumps.length) {
            int next = idx + jumps[idx];
            jumps[idx]++;
            steps++;
            idx = next;
        }
        return steps;
    }

    @Override
    protected Integer solvePartTwo(int[] jumps) {
        int idx = 0;
        int steps = 0;
        while (idx >= 0 && idx < jumps.length) {
            int j = jumps[idx];
            int next = idx + j;
            jumps[idx] += j < 3 ? 1 : -1;
            steps++;
            idx = next;
        }
        return steps;
    }

}

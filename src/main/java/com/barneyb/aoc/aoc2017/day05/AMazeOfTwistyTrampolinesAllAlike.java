package com.barneyb.aoc.aoc2017.day05;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.ArrayList;

public class AMazeOfTwistyTrampolinesAllAlike extends SolvePartOne<int[], Long> {

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
    protected Long solvePartOne(int[] jumps) {
        int idx = 0;
        long steps = 0;
        while (idx >= 0 && idx < jumps.length) {
            int next = idx + jumps[idx];
            jumps[idx]++;
            steps++;
            idx = next;
        }
        return steps;
    }

}

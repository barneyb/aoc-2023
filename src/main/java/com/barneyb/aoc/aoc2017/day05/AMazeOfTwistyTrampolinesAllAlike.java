package com.barneyb.aoc.aoc2017.day05;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;
import java.util.List;

public class AMazeOfTwistyTrampolinesAllAlike extends SolveEachPart<List<Integer>, Integer, Integer> {

    public static void main(String[] args) {
        new AMazeOfTwistyTrampolinesAllAlike().solveAndPrint();
    }

    @Override
    protected List<Integer> buildModel(Input input) {
        ArrayList<Integer> list = new ArrayList<>();
        for (String s : input) {
            list.add(Integer.valueOf(s));
        }
        return list;
    }

    private int[] listToArray(List<Integer> list) {
        int[] arr = new int[list.size()];
        int i = 0;
        for (int j : list) {
            arr[i++] = j;
        }
        return arr;
    }

    @Override
    protected Integer solvePartOne(List<Integer> list) {
        int[] jumps = listToArray(list);
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
    protected Integer solvePartTwo(List<Integer> list) {
        int[] jumps = listToArray(list);
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

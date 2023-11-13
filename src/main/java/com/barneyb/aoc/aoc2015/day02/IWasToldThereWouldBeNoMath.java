package com.barneyb.aoc.aoc2015.day02;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;
import java.util.Collection;

public class IWasToldThereWouldBeNoMath extends SolveEachPart<Collection<Box>, Long, Long> {

    public static void main(String[] args) {
        new IWasToldThereWouldBeNoMath().solveAndPrint();
    }

    @Override
    protected Collection<Box> buildModel(Input input) {
        Collection<Box> boxes = new ArrayList<>();
        for (String line : input) {
            String[] dims = line.split("x");
            boxes.add(new Box(Long.parseLong(dims[0]),
                              Long.parseLong(dims[1]),
                              Long.parseLong(dims[2])));
        }
        return boxes;
    }

    @Override
    protected Long solvePartOne(Collection<Box> boxes) {
        long answer = 0;
        for (Box b : boxes) {
            answer += b.paperRequired();
        }
        return answer;
    }

    @Override
    protected Long solvePartTwo(Collection<Box> boxes) {
        long answer = 0;
        for (Box b : boxes) {
            answer += b.ribbonRequired();
        }
        return answer;
    }

}

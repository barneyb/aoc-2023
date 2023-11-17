package com.barneyb.aoc.aoc2020.day05;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.List;

public class BinaryBoarding extends SolvePartOne<List<BoardingPass>, Integer> {

    public static void main(String[] args) {
        new BinaryBoarding().solveAndPrint();
    }

    @Override
    protected List<BoardingPass> buildModel(Input input) {
        return input.streamLines()
                .map(BoardingPass::of)
                .toList();
    }

    @Override
    protected Integer solvePartOne(List<BoardingPass> boardingPasses) {
        return boardingPasses.stream()
                .mapToInt(BoardingPass::seatId)
                .max()
                .orElseThrow();
    }

}

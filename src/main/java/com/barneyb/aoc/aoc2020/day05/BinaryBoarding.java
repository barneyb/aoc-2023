package com.barneyb.aoc.aoc2020.day05;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.List;

public class BinaryBoarding extends SolveEachPart<List<BoardingPass>, Integer, Integer> {

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

    @Override
    protected Integer solvePartTwo(List<BoardingPass> boardingPasses) {
        int[] ids = boardingPasses.stream()
                .mapToInt(BoardingPass::seatId)
                .sorted()
                .toArray();
        for (int i = ids.length - 2; i >= 0; i--) {
            if (ids[i] + 1 != ids[i + 1]) return ids[i] + 1;
        }
        throw new RuntimeException("No empty seat found");
    }

}

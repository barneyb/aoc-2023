package com.barneyb.aoc.aoc2023.day09;

import com.barneyb.aoc.util.Answers;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveTogether;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MirageMaintenance extends SolveTogether<List<List<Long>>, Long, Long> {

    public static void main(String[] args) {
        new MirageMaintenance().solveAndPrint();
    }

    @Override
    protected List<List<Long>> buildModel(Input input) {
        return input.streamLines()
                .map(l -> Arrays.stream(l.split(" "))
                        .map(Long::parseLong)
                        .toList())
                .toList();
    }

    private Answers<Long, Long> extrapolate(List<Long> seq) {
        List<Long> diffs = new ArrayList<>(seq.size() - 1);
        boolean allSame = true;
        Long prev = seq.get(0);
        for (Long n : seq.subList(1, seq.size())) {
            if (prev.equals(n)) {
                diffs.add(0L);
            } else {
                allSame = false;
                diffs.add(n - prev);
                prev = n;
            }
        }
        if (allSame) {
            return new Answers<>(prev, prev);
        } else {
            Answers<Long, Long> as = extrapolate(diffs);
            return new Answers<>(seq.get(seq.size() - 1) + as.partOne(),
                                 seq.get(0) - as.partTwo());
        }
    }

    @Override
    protected Answers<Long, Long> solveTogether(List<List<Long>> lists) {
        return lists.stream()
                .map(this::extrapolate)
                .reduce((a, b) -> new Answers<>(a.partOne() + b.partOne(),
                                                a.partTwo() + b.partTwo()))
                .orElseThrow();
    }

}

package com.barneyb.aoc.aoc2023.day09;

import com.barneyb.aoc.util.Answers;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveTogether;

import java.util.Arrays;

public class MirageMaintenance extends SolveTogether<long[][], Long, Long> {

    public static void main(String[] args) {
        new MirageMaintenance().solveAndPrint();
    }

    @Override
    protected long[][] buildModel(Input input) {
        return input.streamLines()
                .map(l -> Arrays.stream(l.split(" "))
                        .mapToLong(Long::parseLong)
                        .toArray())
                .toArray(long[][]::new);
    }

    private Answers<Long, Long> extrapolate(long[] seq) {
        long[] diffs = new long[seq.length - 1];
        boolean allSame = true;
        long prev = seq[0];
        for (int i = 0, l = seq.length - 1; i < l; i++) {
            long n = seq[i + 1];
            if (prev != n) {
                allSame = false;
                diffs[i] = n - prev;
                prev = n;
            }
        }
        if (allSame) {
            return new Answers<>(prev, prev);
        } else {
            Answers<Long, Long> as = extrapolate(diffs);
            return new Answers<>(seq[seq.length - 1] + as.partOne(),
                                 seq[0] - as.partTwo());
        }
    }

    @Override
    protected Answers<Long, Long> solveTogether(long[][] lists) {
        return Arrays.stream(lists)
                .map(this::extrapolate)
                .reduce((a, b) -> new Answers<>(a.partOne() + b.partOne(),
                                                a.partTwo() + b.partTwo()))
                .orElseThrow();
    }

}

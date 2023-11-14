package com.barneyb.aoc.aoc2016.day05;

import com.barneyb.aoc.util.Digest;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

public class HowAboutANiceGameOfChess extends SolveEachPart<String, String, String> {

    public static void main(String[] args) {
        new HowAboutANiceGameOfChess().solveAndPrint();
    }

    @Override
    protected String buildModel(Input input) {
        return input.firstLine();
    }

    @Override
    protected String solvePartOne(String doorKey) {
        StringBuilder sb = new StringBuilder(8);
        for (long i = 0; ; i++) {
            byte[] bytes = Digest.md5(doorKey, i);
            if (startsWithFiveZeros(bytes)) {
                sb.append(Integer.toString(bytes[2] & 0x0f, 16));
                if (sb.length() == 8) return sb.toString();
            }
        }
    }

    private boolean startsWithFiveZeros(byte[] bytes) {
        return bytes[0] == 0 && bytes[1] == 0 && (bytes[2] & 0xf0) == 0;
    }

    @Override
    protected String solvePartTwo(String doorKey) {
        StringBuilder sb = new StringBuilder();
        sb.append("        ");
        int chars = 0;
        for (long i = 0; ; i++) {
            byte[] bytes = Digest.md5(doorKey, i);
            if (startsWithFiveZeros(bytes)) {
                int idx = bytes[2] & 0x0f;
                if (idx > 7 || sb.charAt(idx) != ' ') continue;
                char c = Integer.toString(bytes[3] & 0xf0, 16).charAt(0);
                sb.setCharAt(idx, c);
                if (++chars == 8) return sb.toString();
            }
        }
    }

}

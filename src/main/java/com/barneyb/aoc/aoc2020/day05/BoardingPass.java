package com.barneyb.aoc.aoc2020.day05;

public record BoardingPass(int row, int col) {

    public static BoardingPass of(String pass) {
        int row = partition(pass.substring(0, 7), 'F');
        int col = partition(pass.substring(7), 'L');
        return new BoardingPass(row, col);
    }

    private static int partition(String steps, char lowHalf) {
        int lo = 0;
        int hi = (int) Math.pow(2, steps.length());
        for (char c : steps.toCharArray()) {
            int window = (hi - lo) / 2;
            if (c == lowHalf) {
                hi -= window;
            } else { // must be B
                lo += window;
            }
        }
        assert lo == hi - 1; // half open
        return lo;
    }

    public int seatId() {
        return row * 8 + col;
    }

}

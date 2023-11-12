package com.barneyb.aoc.aoc2015.day01;

import com.barneyb.aoc.util.Answers;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveTogether;

public class NotQuiteLisp extends SolveTogether<char[], Integer, Integer> {

    public NotQuiteLisp() {
        super(2015, 1);
    }

    @Override
    protected char[] buildModel(Input input) {
        return input.firstLine()
                .toCharArray();
    }

    @Override
    protected Answers<Integer, Integer> solveTogether(char[] chars) {
        int floor = 0;
        int bPos = 0;
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (c == '(') floor++;
            else if (c == ')') floor--;
            else throw new RuntimeException(String.format(
                        "Unrecognized '%s'",
                        c));
            if (floor == -1 && bPos == 0) bPos = i + 1;
        }
        return new Answers<>(floor, bPos);
    }

    public static void main(String[] args) {
        new NotQuiteLisp().solveAndPrint();
    }

}

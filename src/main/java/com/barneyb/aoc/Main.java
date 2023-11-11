package com.barneyb.aoc;

import com.barneyb.aoc.util.Input;

public class Main {

    public static void main(String[] args) {
        String input = Input.of(2015, 1).firstLine();
        int floor = 0;
        int bPos = 0;
        char[] chars = input.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (c == '(') floor++;
            else if (c == ')') floor--;
            else throw new RuntimeException(String.format(
                        "Unrecognized '%s'",
                        c));
            if (floor == -1 && bPos == 0) bPos = i + 1;
        }
        System.out.println(floor);
        System.out.println(bPos);
    }

}
